#!/usr/bin/env python3
"""Simple Flask web interface for managing ordotools database."""

import sys
import os
import sqlite3
from collections import defaultdict
from typing import Optional, List, Dict, Any

# Add parent directory to path to import ordotools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, jsonify, request, g
from ordotools.tools.db import get_connection
from ordotools.tools.repositories.dioceses_repo import DiocesesRepository
from ordotools.tools.repositories.temporal_repo import TemporalRepository
from ordotools.tools.repositories.sanctoral_repo import SanctoralRepository
from ordotools.tools.repositories.translations_repo import TranslationsRepository

app = Flask(__name__)


def get_db():
    """Get database connection for the current request."""
    if 'db' not in g:
        g.db = get_connection()
    return g.db


def get_repositories():
    """Get all repository instances for the current request."""
    if 'repos' not in g:
        # Repositories create their own connections, so pass None
        g.repos = {
            'dioceses': DiocesesRepository(None),
            'temporal': TemporalRepository(None),
            'sanctoral': SanctoralRepository(None),
            'translations': TranslationsRepository(None)
        }
    return g.repos


def get_languages_list() -> List[str]:
    """Fetch all language codes from translations."""
    try:
        db = get_db()
        cursor = db.execute(
            "SELECT DISTINCT language_code FROM translations ORDER BY language_code"
        )
        return [row['language_code'] for row in cursor.fetchall()]
    except Exception:
        return []


def _collect_unique(values: List[Any]) -> List[Any]:
    """Return sorted unique list from incoming values, preserving numbers ordering."""
    seen = set()
    unique = []
    for value in values:
        if value in (None, '', False):
            continue
        if value not in seen:
            seen.add(value)
            unique.append(value)
    try:
        return sorted(unique)
    except TypeError:
        return unique


@app.teardown_appcontext
def close_db(error):
    """Close database connection at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()
    
    # Close repository connections
    repos = g.pop('repos', None)
    if repos is not None:
        for repo in repos.values():
            if hasattr(repo, 'close'):
                repo.close()


@app.route('/favicon.ico')
def favicon():
    """Return empty response for favicon to prevent 404 errors."""
    return '', 204


@app.route('/api/test-connection')
def test_connection():
    """Test database connection and return basic stats."""
    try:
        db = get_db()
        
        # Get counts from new tables
        temporal_count = db.execute("SELECT COUNT(*) as count FROM temporal_feasts").fetchone()['count']
        sanctoral_count = db.execute("SELECT COUNT(*) as count FROM sanctoral_feasts_new").fetchone()['count']
        countries_count = db.execute("SELECT COUNT(*) as count FROM countries").fetchone()['count']
        dioceses_count = db.execute("SELECT COUNT(*) as count FROM dioceses").fetchone()['count']
        translations_count = db.execute("SELECT COUNT(*) as count FROM translations").fetchone()['count']
        
        return jsonify({
            'status': 'success',
            'stats': {
                'temporal_feasts': temporal_count,
                'sanctoral_feasts': sanctoral_count,
                'countries': countries_count,
                'dioceses': dioceses_count,
                'translations': translations_count,
                'total_feasts': temporal_count + sanctoral_count
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/countries')
@app.route('/api/countries', methods=['GET', 'POST'])
def get_countries():
    """Get or create countries."""
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        code = (data.get('code') or '').strip().upper()
        name_latin = (data.get('name_latin') or '').strip()
        name_english = (data.get('name_english') or '').strip() or None
        
        if not code or not name_latin:
            return jsonify({'error': 'Code and Latin name are required.'}), 400
        
        try:
            db = get_db()
            with db:
                cursor = db.execute(
                    """
                    INSERT INTO countries (code, name_latin, name_english)
                    VALUES (?, ?, ?)
                    """,
                    (code, name_latin, name_english)
                )
            return jsonify({
                'status': 'success',
                'id': cursor.lastrowid,
                'code': code,
                'name_latin': name_latin,
                'name_english': name_english
            }), 201
        except sqlite3.IntegrityError as exc:
            return jsonify({'error': f'Unable to add country: {exc}'}), 400
    
    try:
        repos = get_repositories()
        countries = repos['dioceses'].get_all_countries()
        return jsonify([{
            'id': c['id'],
            'code': c['code'],
            'name_latin': c['name_latin'],
            'name_english': c['name_english']
        } for c in countries])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/dioceses', methods=['GET', 'POST'])
def get_dioceses_api():
    """Get or create dioceses."""
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        code = (data.get('code') or '').strip().lower()
        name_latin = (data.get('name_latin') or '').strip()
        name_english = (data.get('name_english') or '').strip() or None
        country_id_raw: Optional[str] = data.get('country_id')
        country_id = int(country_id_raw) if country_id_raw else None
        
        if not code or not name_latin:
            return jsonify({'error': 'Code and Latin name are required.'}), 400
        
        try:
            db = get_db()
            with db:
                cursor = db.execute(
                    """
                    INSERT INTO dioceses (code, name_latin, name_english, country_id)
                    VALUES (?, ?, ?, ?)
                    """,
                    (code, name_latin, name_english, country_id)
                )
            return jsonify({
                'status': 'success',
                'id': cursor.lastrowid,
                'code': code,
                'name_latin': name_latin,
                'name_english': name_english,
                'country_id': country_id
            }), 201
        except sqlite3.IntegrityError as exc:
            return jsonify({'error': f'Unable to add diocese: {exc}'}), 400
    
    try:
        repos = get_repositories()
        country_code = request.args.get('country', None)
        
        if country_code:
            dioceses = repos['dioceses'].get_dioceses_by_country(country_code)
        else:
            dioceses = repos['dioceses'].get_all_dioceses()
        
        return jsonify([{
            'id': d['id'],
            'code': d['code'],
            'name_latin': d['name_latin'],
            'name_english': d['name_english'],
            'country_id': d.get('country_id')
        } for d in dioceses])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/temporal/feasts', methods=['GET', 'POST'])
def get_temporal_feasts():
    """Get or create temporal feasts."""
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        feast_id = (data.get('id') or '').strip()
        rank_numeric_raw = data.get('rank_numeric')
        rank_verbose = (data.get('rank_verbose') or '').strip()
        color = (data.get('color') or '').strip()
        office_type = (data.get('office_type') or '').strip() or None
        
        try:
            rank_numeric = int(rank_numeric_raw)
        except (TypeError, ValueError):
            rank_numeric = None
        
        if not feast_id or rank_numeric is None or not rank_verbose or not color:
            return jsonify({'error': 'ID, rank numeric, rank verbose, and color are required.'}), 400
        
        try:
            db = get_db()
            with db:
                db.execute(
                    """
                    INSERT INTO temporal_feasts (id, rank_numeric, rank_verbose, color, office_type)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (feast_id, rank_numeric, rank_verbose, color, office_type)
                )
            return jsonify({
                'status': 'success',
                'id': feast_id
            }), 201
        except sqlite3.IntegrityError as exc:
            return jsonify({'error': f'Unable to add temporal feast: {exc}'}), 400
    
    try:
        repos = get_repositories()
        feasts = repos['temporal'].get_all_feasts()
        
        # Limit results for API
        limit = int(request.args.get('limit', 50))
        feasts_list = list(feasts.items())[:limit]
        
        return jsonify([{
            'id': feast_id,
            'rank': feast['rank'],
            'color': feast['color'],
            'office_type': feast.get('office_type')
        } for feast_id, feast in feasts_list])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/sanctoral/feasts', methods=['GET', 'POST'])
def get_sanctoral_feasts():
    """Get sanctoral feasts for a diocese and date or create new ones."""
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        
        diocese_id_raw = data.get('diocese_id')
        try:
            diocese_id = int(diocese_id_raw) if diocese_id_raw else None
        except (TypeError, ValueError):
            return jsonify({'error': 'Diocese ID must be an integer.'}), 400
        
        rank_numeric_raw = data.get('rank_numeric')
        rank_verbose = (data.get('rank_verbose') or '').strip()
        color = (data.get('color') or '').strip()
        office_type = (data.get('office_type') or '').strip() or None
        month_raw = data.get('month')
        day_raw = data.get('day')
        assignment_diocese_raw = data.get('assignment_diocese_id')
        
        try:
            rank_numeric = int(rank_numeric_raw)
            month = int(month_raw)
            day = int(day_raw)
        except (TypeError, ValueError):
            return jsonify({'error': 'Rank numeric, month, and day must be integers.'}), 400
        
        if not rank_verbose or not color:
            return jsonify({'error': 'Rank verbose and color are required.'}), 400
        
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return jsonify({'error': 'Month must be 1-12 and day 1-31.'}), 400
        
        try:
            assignment_diocese_id = int(assignment_diocese_raw) if assignment_diocese_raw else None
        except (TypeError, ValueError):
            return jsonify({'error': 'Assignment diocese ID must be an integer.'}), 400
        
        try:
            db = get_db()
            with db:
                max_row = db.execute(
                    "SELECT COALESCE(MAX(id), 0) AS max_id FROM sanctoral_feasts_new"
                ).fetchone()
                current_max = max_row['max_id'] if max_row else 0
                new_id = current_max + 100 if current_max else 100
                
                db.execute(
                    """
                    INSERT INTO sanctoral_feasts_new (
                        id, diocese_id, rank_numeric, rank_verbose, color, office_type
                    ) VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (new_id, diocese_id, rank_numeric, rank_verbose, color, office_type)
                )
                
                db.execute(
                    """
                    INSERT INTO feast_date_assignments (feast_id, month, day, diocese_id)
                    VALUES (?, ?, ?, ?)
                    """,
                    (new_id, month, day, assignment_diocese_id)
                )
            
            return jsonify({
                'status': 'success',
                'id': new_id
            }), 201
        except sqlite3.IntegrityError as exc:
            return jsonify({'error': f'Unable to add sanctoral feast: {exc}'}), 400
        except Exception as exc:  # pragma: no cover - generic catch for runtime errors
            return jsonify({'error': str(exc)}), 500
    
    try:
        repos = get_repositories()
        diocese_code = request.args.get('diocese', 'roman')
        month = request.args.get('month')
        day = request.args.get('day')
        
        if month and day:
            feasts = repos['sanctoral'].get_feasts_for_date(int(month), int(day), diocese_code)
        else:
            # Get full calendar
            calendar = repos['sanctoral'].get_year_calendar(diocese_code)
            # Convert to list format
            feasts = []
            for date_key, feast in calendar.items():
                feasts.append({
                    'month': date_key.month,
                    'day': date_key.day,
                    **feast
                })
            # Limit results
            limit = int(request.args.get('limit', 50))
            feasts = feasts[:limit]
        
        return jsonify(feasts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/feast-dates', methods=['POST'])
def create_feast_date():
    """Create feast date assignments."""
    data = request.get_json(silent=True) or {}
    feast_id_raw = data.get('feast_id')
    month_raw = data.get('month')
    day_raw = data.get('day')
    diocese_id_raw = data.get('diocese_id')
    
    try:
        feast_id = int(feast_id_raw)
        month = int(month_raw)
        day = int(day_raw)
    except (TypeError, ValueError):
        return jsonify({'error': 'Feast ID, month, and day must be integers.'}), 400
    
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return jsonify({'error': 'Month must be 1-12 and day 1-31.'}), 400
    
    try:
        diocese_id = int(diocese_id_raw) if diocese_id_raw else None
    except (TypeError, ValueError):
        return jsonify({'error': 'Diocese ID must be an integer.'}), 400
    
    try:
        db = get_db()
        with db:
            cursor = db.execute(
                """
                INSERT INTO feast_date_assignments (feast_id, month, day, diocese_id)
                VALUES (?, ?, ?, ?)
                """,
                (feast_id, month, day, diocese_id)
            )
        return jsonify({
            'status': 'success',
            'id': cursor.lastrowid
        }), 201
    except sqlite3.IntegrityError as exc:
        return jsonify({'error': f'Unable to add date assignment: {exc}'}), 400


@app.route('/api/translations', methods=['POST'])
def create_translation():
    """Create a translation record."""
    data = request.get_json(silent=True) or {}
    feast_id = (data.get('feast_id') or '').strip()
    feast_type = (data.get('feast_type') or '').strip().lower()
    language_code = (data.get('language_code') or '').strip().lower()
    translation = (data.get('translation') or '').strip()
    is_default = 1 if str(data.get('is_default', '')).lower() in {'1', 'true', 'on', 'yes'} else 0
    
    if not feast_id or not feast_type or not language_code or not translation:
        return jsonify({'error': 'Feast, type, language, and translation are required.'}), 400
    
    if feast_type not in {'temporal', 'sanctoral'}:
        return jsonify({'error': 'Feast type must be "temporal" or "sanctoral".'}), 400
    
    try:
        db = get_db()
        with db:
            cursor = db.execute(
                """
                INSERT INTO translations (feast_id, feast_type, language_code, translation, is_default)
                VALUES (?, ?, ?, ?, ?)
                """,
                (feast_id, feast_type, language_code, translation, is_default)
            )
        return jsonify({
            'status': 'success',
            'id': cursor.lastrowid
        }), 201
    except sqlite3.IntegrityError as exc:
        return jsonify({'error': f'Unable to add translation: {exc}'}), 400


def _fetch_feasts_overview() -> List[Dict[str, Any]]:
    """Return combined overview of temporal and sanctoral feasts."""
    db = get_db()
    overview: List[Dict[str, Any]] = []
    
    temporal_rows = db.execute(
        """
        SELECT f.id, f.rank_numeric, f.rank_verbose, f.color, f.office_type,
               COALESCE(t.translation, f.id) AS name_latin
        FROM temporal_feasts f
        LEFT JOIN translations t
            ON t.feast_id = f.id
           AND t.feast_type = 'temporal'
           AND t.language_code = 'la'
        ORDER BY f.id
        """
    ).fetchall()
    for row in temporal_rows:
        overview.append({
            'feast_type': 'temporal',
            'id': row['id'],
            'display_id': str(row['id']),
            'rank_numeric': row['rank_numeric'],
            'rank_verbose': row['rank_verbose'],
            'color': row['color'],
            'office_type': row['office_type'] or '',
            'name_latin': row['name_latin'] or row['id'],
            'appears_in_calendar': False,
            'month': None,
            'day': None,
            'calendar_diocese_code': None,
            'calendar_country_code': None,
            'owning_diocese_code': None,
            'owning_country_code': None,
            'assignment_summary': ''
        })
    
    sanctoral_rows = db.execute(
        """
        SELECT sf.id,
               sf.rank_numeric,
               sf.rank_verbose,
               sf.color,
               sf.office_type,
               COALESCE(ts.translation, 'Feast ' || sf.id) AS name_latin,
               owner.code AS owning_diocese_code,
               owner_country.code AS owning_country_code,
               fda.id AS assignment_id,
               fda.month,
               fda.day,
               assign_diocese.code AS assignment_diocese_code,
               assign_country.code AS assignment_country_code
        FROM sanctoral_feasts_new sf
        LEFT JOIN translations ts
            ON ts.feast_id = CAST(sf.id AS TEXT)
           AND ts.feast_type = 'sanctoral'
           AND ts.language_code = 'la'
        LEFT JOIN dioceses owner ON sf.diocese_id = owner.id
        LEFT JOIN countries owner_country ON owner.country_id = owner_country.id
        LEFT JOIN feast_date_assignments fda ON sf.id = fda.feast_id
        LEFT JOIN dioceses assign_diocese ON fda.diocese_id = assign_diocese.id
        LEFT JOIN countries assign_country ON assign_diocese.country_id = assign_country.id
        ORDER BY sf.id, fda.month, fda.day, fda.id
        """
    ).fetchall()
    
    sanctoral_map: Dict[int, Dict[str, Any]] = {}
    for row in sanctoral_rows:
        entry = sanctoral_map.setdefault(row['id'], {
            'feast_type': 'sanctoral',
            'id': row['id'],
            'display_id': str(row['id']),
            'rank_numeric': row['rank_numeric'],
            'rank_verbose': row['rank_verbose'],
            'color': row['color'],
            'office_type': row['office_type'] or '',
            'name_latin': row['name_latin'] or f"Feast {row['id']}",
            'owning_diocese_code': row['owning_diocese_code'],
            'owning_country_code': row['owning_country_code'],
            'assignments': []
        })
        
        if row['assignment_id'] is not None:
            entry['assignments'].append({
                'assignment_id': row['assignment_id'],
                'month': row['month'],
                'day': row['day'],
                'diocese_code': row['assignment_diocese_code'] or 'roman',
                'country_code': row['assignment_country_code'],
            })
    
    for entry in sanctoral_map.values():
        assignments = entry.pop('assignments')
        first_assignment = assignments[0] if assignments else {}
        entry['appears_in_calendar'] = bool(assignments)
        entry['month'] = first_assignment.get('month')
        entry['day'] = first_assignment.get('day')
        entry['calendar_diocese_code'] = first_assignment.get('diocese_code')
        entry['calendar_country_code'] = first_assignment.get('country_code')
        entry['assignments'] = assignments
        entry['assignment_summary'] = ", ".join(
            f"{assignment['month']:02d}-{assignment['day']:02d} ({assignment['diocese_code']})"
            for assignment in assignments
        ) if assignments else ''
        overview.append(entry)
    
    overview.sort(key=lambda item: str(item.get('display_id') or item.get('id')))
    return overview


def _get_feast_metadata() -> Dict[str, Any]:
    """Collect metadata for feast forms and dropdowns."""
    db = get_db()
    metadata: Dict[str, Any] = {}
    
    temporal_ids = [row['id'] for row in db.execute(
        "SELECT id FROM temporal_feasts ORDER BY id"
    ).fetchall()]
    sanctoral_ids = [str(row['id']) for row in db.execute(
        "SELECT id FROM sanctoral_feasts_new ORDER BY id"
    ).fetchall()]
    metadata['temporal_ids'] = temporal_ids
    metadata['sanctoral_ids'] = sanctoral_ids
    metadata['all_ids'] = temporal_ids + sanctoral_ids
    
    ranks_numeric: List[Any] = []
    ranks_verbose: List[Any] = []
    colors: List[Any] = []
    office_types: List[Any] = []
    
    for table in ('temporal_feasts', 'sanctoral_feasts_new'):
        rows = db.execute(
            f"SELECT rank_numeric, rank_verbose, color, office_type FROM {table}"
        ).fetchall()
        for row in rows:
            ranks_numeric.append(row['rank_numeric'])
            ranks_verbose.append(row['rank_verbose'])
            colors.append(row['color'])
            office_types.append(row['office_type'])
    
    metadata['rank_numeric_values'] = _collect_unique(ranks_numeric)
    metadata['rank_verbose_values'] = _collect_unique(ranks_verbose)
    metadata['color_values'] = _collect_unique(colors)
    metadata['office_type_values'] = _collect_unique(office_types)
    
    months = [row['month'] for row in db.execute(
        "SELECT DISTINCT month FROM feast_date_assignments ORDER BY month"
    ).fetchall()]
    days = [row['day'] for row in db.execute(
        "SELECT DISTINCT day FROM feast_date_assignments ORDER BY day"
    ).fetchall()]
    metadata['month_values'] = _collect_unique(months)
    metadata['day_values'] = _collect_unique(days)
    
    dioceses = db.execute(
        """
        SELECT d.id, d.code, d.name_latin, d.name_english, c.code AS country_code
        FROM dioceses d
        LEFT JOIN countries c ON d.country_id = c.id
        ORDER BY d.code
        """
    ).fetchall()
    metadata['dioceses'] = [{
        'id': row['id'],
        'code': row['code'],
        'name_latin': row['name_latin'],
        'name_english': row['name_english'],
        'country_code': row['country_code']
    } for row in dioceses]
    
    countries = db.execute(
        "SELECT id, code, name_latin, name_english FROM countries ORDER BY code"
    ).fetchall()
    metadata['countries'] = [{
        'id': row['id'],
        'code': row['code'],
        'name_latin': row['name_latin'],
        'name_english': row['name_english']
    } for row in countries]
    
    calendar_dioceses = set()
    for row in db.execute(
        "SELECT DISTINCT diocese_id FROM feast_date_assignments WHERE diocese_id IS NOT NULL"
    ).fetchall():
        calendar_dioceses.add(row['diocese_id'])
    calendar_codes = []
    if calendar_dioceses:
        placeholders = ",".join("?" for _ in calendar_dioceses)
        query = f"SELECT code FROM dioceses WHERE id IN ({placeholders})"
        codes = db.execute(query, tuple(calendar_dioceses)).fetchall()
        calendar_codes = [row['code'] for row in codes]
    if db.execute(
        "SELECT COUNT(*) AS cnt FROM feast_date_assignments WHERE diocese_id IS NULL"
    ).fetchone()['cnt']:
        calendar_codes.append('roman')
    metadata['calendar_diocese_codes'] = sorted(set(calendar_codes))
    
    return metadata


def _fetch_temporal_detail(feast_id: str) -> Optional[Dict[str, Any]]:
    """Return full detail for a temporal feast."""
    db = get_db()
    row = db.execute(
        """
        SELECT f.id, f.rank_numeric, f.rank_verbose, f.color, f.office_type,
               COALESCE(t.translation, f.id) AS name_latin
        FROM temporal_feasts f
        LEFT JOIN translations t
            ON t.feast_id = f.id
           AND t.feast_type = 'temporal'
           AND t.language_code = 'la'
        WHERE f.id = ?
        """,
        (feast_id,)
    ).fetchone()
    if not row:
        return None
    return {
        'feast_type': 'temporal',
        'id': row['id'],
        'display_id': str(row['id']),
        'rank_numeric': row['rank_numeric'],
        'rank_verbose': row['rank_verbose'],
        'color': row['color'],
        'office_type': row['office_type'] or '',
        'name_latin': row['name_latin'] or row['id'],
    }


def _fetch_sanctoral_detail(feast_id: int) -> Optional[Dict[str, Any]]:
    """Return full detail for a sanctoral feast including assignments."""
    db = get_db()
    row = db.execute(
        """
        SELECT sf.id,
               sf.rank_numeric,
               sf.rank_verbose,
               sf.color,
               sf.office_type,
               sf.diocese_id,
               owner.code AS owning_diocese_code,
               owner.name_latin AS owning_diocese_name_latin,
               owner.name_english AS owning_diocese_name_english,
               owner_country.code AS owning_country_code,
               COALESCE(t.translation, 'Feast ' || sf.id) AS name_latin
        FROM sanctoral_feasts_new sf
        LEFT JOIN translations t
            ON t.feast_id = CAST(sf.id AS TEXT)
           AND t.feast_type = 'sanctoral'
           AND t.language_code = 'la'
        LEFT JOIN dioceses owner ON sf.diocese_id = owner.id
        LEFT JOIN countries owner_country ON owner.country_id = owner_country.id
        WHERE sf.id = ?
        """,
        (feast_id,)
    ).fetchone()
    if not row:
        return None
    
    assignments = db.execute(
        """
        SELECT fda.id,
               fda.month,
               fda.day,
               fda.diocese_id,
               COALESCE(assign_diocese.code, 'roman') AS diocese_code,
               assign_diocese.name_latin AS diocese_name_latin,
               assign_diocese.name_english AS diocese_name_english,
               assign_country.code AS country_code
        FROM feast_date_assignments fda
        LEFT JOIN dioceses assign_diocese ON fda.diocese_id = assign_diocese.id
        LEFT JOIN countries assign_country ON assign_diocese.country_id = assign_country.id
        WHERE fda.feast_id = ?
        ORDER BY fda.month, fda.day, fda.id
        """,
        (feast_id,)
    ).fetchall()
    
    assignment_list = [{
        'assignment_id': item['id'],
        'month': item['month'],
        'day': item['day'],
        'diocese_id': item['diocese_id'],
        'diocese_code': item['diocese_code'],
        'diocese_name_latin': item['diocese_name_latin'],
        'diocese_name_english': item['diocese_name_english'],
        'country_code': item['country_code'],
    } for item in assignments]
    
    first_assignment = assignment_list[0] if assignment_list else None
    return {
        'feast_type': 'sanctoral',
        'id': row['id'],
        'display_id': str(row['id']),
        'rank_numeric': row['rank_numeric'],
        'rank_verbose': row['rank_verbose'],
        'color': row['color'],
        'office_type': row['office_type'] or '',
        'diocese_id': row['diocese_id'],
        'owning_diocese_code': row['owning_diocese_code'],
        'owning_country_code': row['owning_country_code'],
        'name_latin': row['name_latin'],
        'assignments': assignment_list,
        'appears_in_calendar': bool(assignment_list),
        'primary_assignment': first_assignment
    }


def _update_temporal_feast(feast_id: str, payload: Dict[str, Any]):
    """Update an existing temporal feast."""
    target_id = feast_id
    new_id = (payload.get('id') or feast_id).strip()
    
    try:
        rank_numeric = int(payload.get('rank_numeric'))
    except (TypeError, ValueError):
        return {'error': 'Rank numeric must be an integer.'}, 400
    
    rank_verbose = (payload.get('rank_verbose') or '').strip()
    color = (payload.get('color') or '').strip()
    office_type = (payload.get('office_type') or '').strip() or None
    
    if not rank_verbose or not color:
        return {'error': 'Rank verbose and color are required.'}, 400
    
    db = get_db()
    try:
        with db:
            if new_id != feast_id:
                existing = db.execute(
                    "SELECT 1 FROM temporal_feasts WHERE id = ?",
                    (new_id,)
                ).fetchone()
                if existing:
                    return {'error': 'A temporal feast with that ID already exists.'}, 409
                db.execute(
                    """
                    UPDATE temporal_feasts
                    SET id = ?, rank_numeric = ?, rank_verbose = ?, color = ?, office_type = ?
                    WHERE id = ?
                    """,
                    (new_id, rank_numeric, rank_verbose, color, office_type, feast_id)
                )
                db.execute(
                    """
                    UPDATE translations
                    SET feast_id = ?
                    WHERE feast_type = 'temporal' AND feast_id = ?
                    """,
                    (new_id, feast_id)
                )
                target_id = new_id
            else:
                db.execute(
                    """
                    UPDATE temporal_feasts
                    SET rank_numeric = ?, rank_verbose = ?, color = ?, office_type = ?
                    WHERE id = ?
                    """,
                    (rank_numeric, rank_verbose, color, office_type, feast_id)
                )
    except sqlite3.IntegrityError as exc:
        return {'error': f'Unable to update temporal feast: {exc}'}, 400
    
    detail = _fetch_temporal_detail(target_id)
    return {'status': 'success', 'feast': detail}, 200


def _update_sanctoral_feast(feast_id: int, payload: Dict[str, Any]):
    """Update an existing sanctoral feast and its primary assignment."""
    target_id = feast_id
    
    if 'id' in payload and payload['id'] not in (None, '', feast_id):
        try:
            requested_id = int(payload['id'])
        except (TypeError, ValueError):
            return {'error': 'Sanctoral feast ID must be an integer.'}, 400
        if requested_id != feast_id:
            return {'error': 'Sanctoral feast IDs are immutable.'}, 409
    
    try:
        rank_numeric = int(payload.get('rank_numeric'))
    except (TypeError, ValueError):
        return {'error': 'Rank numeric must be an integer.'}, 400
    
    rank_verbose = (payload.get('rank_verbose') or '').strip()
    color = (payload.get('color') or '').strip()
    office_type = (payload.get('office_type') or '').strip() or None
    
    diocese_id_raw = payload.get('diocese_id')
    if diocese_id_raw in (None, '', 'null'):
        diocese_id = None
    else:
        try:
            diocese_id = int(diocese_id_raw)
        except (TypeError, ValueError):
            return {'error': 'Owning diocese must be an integer ID or empty.'}, 400
    
    appears_in_calendar = bool(payload.get('appears_in_calendar'))
    assignment_payload = payload.get('assignment') or {}
    
    if appears_in_calendar:
        try:
            month = int(assignment_payload.get('month'))
            day = int(assignment_payload.get('day'))
        except (TypeError, ValueError):
            return {'error': 'Month and day must be integers when the feast appears in the calendar.'}, 400
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return {'error': 'Month must be 1-12 and day 1-31.'}, 400
        
        assignment_diocese_raw = assignment_payload.get('diocese_id')
        if assignment_diocese_raw in (None, '', 'roman', 'null'):
            assignment_diocese_id = None
        else:
            try:
                assignment_diocese_id = int(assignment_diocese_raw)
            except (TypeError, ValueError):
                return {'error': 'Assignment diocese must be an integer ID or blank for Roman calendar.'}, 400
        
        assignment_id_raw = assignment_payload.get('assignment_id')
        try:
            assignment_id = int(assignment_id_raw) if assignment_id_raw else None
        except (TypeError, ValueError):
            return {'error': 'Assignment ID must be an integer when provided.'}, 400
    else:
        month = day = None
        assignment_diocese_id = None
        assignment_id = None
    
    if not rank_verbose or not color:
        return {'error': 'Rank verbose and color are required.'}, 400
    
    db = get_db()
    try:
        with db:
            db.execute(
                """
                UPDATE sanctoral_feasts_new
                SET rank_numeric = ?, rank_verbose = ?, color = ?, office_type = ?, diocese_id = ?
                WHERE id = ?
                """,
                (rank_numeric, rank_verbose, color, office_type, diocese_id, feast_id)
            )
            target_id = feast_id
            
            if appears_in_calendar:
                if assignment_id:
                    db.execute(
                        """
                        UPDATE feast_date_assignments
                        SET month = ?, day = ?, diocese_id = ?
                        WHERE id = ? AND feast_id = ?
                        """,
                        (month, day, assignment_diocese_id, assignment_id, target_id)
                    )
                else:
                    db.execute(
                        """
                        INSERT INTO feast_date_assignments (feast_id, month, day, diocese_id)
                        VALUES (?, ?, ?, ?)
                        """,
                        (target_id, month, day, assignment_diocese_id)
                    )
            else:
                db.execute(
                    "DELETE FROM feast_date_assignments WHERE feast_id = ?",
                    (target_id,)
                )
    except sqlite3.IntegrityError as exc:
        return {'error': f'Unable to update sanctoral feast: {exc}'}, 400
    
    detail = _fetch_sanctoral_detail(target_id)
    return {'status': 'success', 'feast': detail}, 200


@app.route('/feasts')
def feasts_view():
    """Spreadsheet-style feast management view."""
    metadata = _get_feast_metadata()
    languages = get_languages_list()
    return render_template(
        'feasts.html',
        metadata=metadata,
        languages=languages or ['la']
    )


@app.route('/api/feasts/overview')
def api_feasts_overview():
    """Return combined overview for temporal and sanctoral feasts."""
    try:
        return jsonify({'feasts': _fetch_feasts_overview()})
    except Exception as exc:
        return jsonify({'error': str(exc)}), 500


@app.route('/api/feasts/metadata')
def api_feasts_metadata():
    """Return metadata for feast-related dropdowns."""
    try:
        return jsonify(_get_feast_metadata())
    except Exception as exc:
        return jsonify({'error': str(exc)}), 500


@app.route('/api/feasts/<feast_type>/<feast_id>', methods=['GET', 'PUT'])
def api_feast_detail(feast_type: str, feast_id: str):
    """Fetch or update a feast by type."""
    feast_type = feast_type.lower()
    if feast_type not in {'temporal', 'sanctoral'}:
        return jsonify({'error': 'Feast type must be "temporal" or "sanctoral".'}), 400
    
    if request.method == 'GET':
        if feast_type == 'temporal':
            detail = _fetch_temporal_detail(feast_id)
        else:
            try:
                detail = _fetch_sanctoral_detail(int(feast_id))
            except ValueError:
                return jsonify({'error': 'Sanctoral feast ID must be numeric.'}), 400
        if not detail:
            return jsonify({'error': 'Feast not found.'}), 404
        return jsonify(detail)
    
    # PUT/update
    payload = request.get_json(silent=True) or {}
    if feast_type == 'temporal':
        return _update_temporal_feast(feast_id, payload)
    try:
        numeric_id = int(feast_id)
    except ValueError:
        return jsonify({'error': 'Sanctoral feast ID must be numeric.'}), 400
    return _update_sanctoral_feast(numeric_id, payload)


@app.route('/api/browse/temporal')
def browse_temporal():
    """Browse temporal feasts with pagination."""
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))
    language = request.args.get('language', 'la')
    
    try:
        repos = get_repositories()
        all_feasts = repos['temporal'].get_all_feasts()
        
        # Convert to list for pagination with translations
        feasts_list = []
        for feast_id, feast_data in all_feasts.items():
            feast_dict = {'id': feast_id, **feast_data}
            
            # Get translation
            translation = repos['translations'].get_translation(
                feast_id, 'temporal', language
            )
            if translation:
                feast_dict['name'] = translation
            else:
                feast_dict['name'] = feast_id
            
            feasts_list.append(feast_dict)
        
        total = len(feasts_list)
        
        # Paginate
        start = (page - 1) * per_page
        end = start + per_page
        page_feasts = feasts_list[start:end]
        
        total_pages = (total + per_page - 1) // per_page
        
        return jsonify({
            'feasts': page_feasts,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': total_pages
            },
            'type': 'temporal',
            'language': language
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/browse/sanctoral')
def browse_sanctoral():
    """Browse sanctoral feasts with pagination and filtering."""
    diocese_code = request.args.get('diocese', 'roman')
    unique_only = request.args.get('unique_only', 'false').lower() == 'true'
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))
    language = request.args.get('language', 'la')
    
    try:
        repos = get_repositories()
        db = get_db()
        
        # Build query based on unique_only flag
        if unique_only and diocese_code != 'roman':
            # Get only diocese-specific feasts
            cursor = db.execute(
                """
                SELECT sf.*, fda.month, fda.day, d.code as diocese_code
                FROM sanctoral_feasts_new sf
                JOIN feast_date_assignments fda ON sf.id = fda.feast_id
                JOIN dioceses d ON fda.diocese_id = d.id
                WHERE d.code = ?
                ORDER BY fda.month, fda.day
                """,
                (diocese_code,)
            )
        elif diocese_code == 'roman':
            # Get Roman feasts
            cursor = db.execute(
                """
                SELECT sf.*, fda.month, fda.day, 'roman' as diocese_code
                FROM sanctoral_feasts_new sf
                JOIN feast_date_assignments fda ON sf.id = fda.feast_id
                WHERE fda.diocese_id IS NULL
                ORDER BY fda.month, fda.day
                """
            )
        else:
            # Get all feasts for diocese (Roman + unique)
            cursor = db.execute(
                """
                SELECT sf.*, fda.month, fda.day, COALESCE(d.code, 'roman') as diocese_code
                FROM sanctoral_feasts_new sf
                JOIN feast_date_assignments fda ON sf.id = fda.feast_id
                LEFT JOIN dioceses d ON fda.diocese_id = d.id
                WHERE fda.diocese_id IS NULL OR d.code = ?
                ORDER BY fda.month, fda.day
                """,
                (diocese_code,)
            )
        
        # Convert to list with translations
        feasts_list = []
        for row in cursor.fetchall():
            feast_dict = {
                'month': row['month'],
                'day': row['day'],
                'id': row['id'],
                'rank': [row['rank_numeric'], row['rank_verbose']],
                'color': row['color'],
                'office_type': row['office_type'] if row['office_type'] else False,
                'diocese_source': row['diocese_code']
            }
            
            # Get translation
            translation = repos['translations'].get_translation(
                str(row['id']), 'sanctoral', language
            )
            if translation:
                feast_dict['name'] = translation
            else:
                feast_dict['name'] = f"Feast {row['id']}"
            
            feasts_list.append(feast_dict)
        
        total = len(feasts_list)
        
        # Paginate
        start = (page - 1) * per_page
        end = start + per_page
        page_feasts = feasts_list[start:end]
        
        total_pages = (total + per_page - 1) // per_page
        
        return jsonify({
            'feasts': page_feasts,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': total_pages
            },
            'type': 'sanctoral',
            'diocese': diocese_code,
            'unique_only': unique_only,
            'language': language
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/browse/dioceses')
def browse_dioceses():
    """Browse dioceses with pagination."""
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))
    
    try:
        repos = get_repositories()
        dioceses = repos['dioceses'].get_all_dioceses()
        
        # Get country names for each diocese
        for diocese in dioceses:
            if diocese.get('country_id'):
                country = repos['dioceses'].get_country_by_id(diocese['country_id'])
                diocese['country_name'] = country.get('name_english') if country else None
            else:
                diocese['country_name'] = None
        
        total = len(dioceses)
        
        # Paginate
        start = (page - 1) * per_page
        end = start + per_page
        page_dioceses = dioceses[start:end]
        
        total_pages = (total + per_page - 1) // per_page
        
        return jsonify({
            'dioceses': page_dioceses,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': total_pages
            },
            'type': 'dioceses'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/browse/countries')
def browse_countries():
    """Browse countries with pagination."""
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))
    
    try:
        repos = get_repositories()
        countries = repos['dioceses'].get_all_countries()
        
        total = len(countries)
        
        # Paginate
        start = (page - 1) * per_page
        end = start + per_page
        page_countries = countries[start:end]
        
        total_pages = (total + per_page - 1) // per_page
        
        return jsonify({
            'countries': page_countries,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': total_pages
            },
            'type': 'countries'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/browse/translations')
def browse_translations():
    """Browse translations with pagination and filtering."""
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))
    feast_type = request.args.get('feast_type', '')
    language_code = request.args.get('language', '')
    
    try:
        db = get_db()
        
        # Build query
        query = "SELECT * FROM translations"
        count_query = "SELECT COUNT(*) as total FROM translations"
        params = []
        conditions = []
        
        if feast_type:
            conditions.append("feast_type = ?")
            params.append(feast_type)
        
        if language_code:
            conditions.append("language_code = ?")
            params.append(language_code)
        
        if conditions:
            where_clause = " WHERE " + " AND ".join(conditions)
            query += where_clause
            count_query += where_clause
        
        # Get total count
        total = db.execute(count_query, params).fetchone()['total']
        
        # Get paginated results
        offset = (page - 1) * per_page
        query += " ORDER BY feast_type, feast_id, language_code LIMIT ? OFFSET ?"
        params.extend([per_page, offset])
        
        cursor = db.execute(query, params)
        translations = [dict(row) for row in cursor.fetchall()]
        
        total_pages = (total + per_page - 1) // per_page
        
        return jsonify({
            'translations': translations,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': total_pages
            },
            'type': 'translations',
            'feast_type': feast_type,
            'language': language_code
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/languages')
def get_languages():
    """Get list of unique language codes."""
    try:
        db = get_db()
        cursor = db.execute(
            "SELECT DISTINCT language_code FROM translations ORDER BY language_code"
        )
        languages = [row['language_code'] for row in cursor.fetchall()]
        return jsonify(languages)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("Starting Ordotools Web Interface...")
    # Test database connection on startup
    test_conn = get_connection()
    db_path = test_conn.execute('PRAGMA database_list').fetchone()[2]
    print(f"Database path: {db_path}")
    test_conn.close()
    app.run(debug=True, host='127.0.0.1', port=5000)
