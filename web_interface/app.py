#!/usr/bin/env python3
"""Simple Flask web interface for managing ordotools database."""

import sys
import os
import sqlite3
from collections import defaultdict
from typing import Optional, List, Dict, Any

# Add parent directory to path to import ordotools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, jsonify, request, g, redirect, url_for, flash
from ordotools.tools.db import get_connection
from ordotools.tools.repositories.dioceses_repo import DiocesesRepository
from ordotools.tools.repositories.temporal_repo import TemporalRepository
from ordotools.tools.repositories.sanctoral_repo import SanctoralRepository
from ordotools.tools.repositories.translations_repo import TranslationsRepository
from forms import TemporalFeastForm, SanctoralFeastForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-please-change-in-production'


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


@app.route('/temporal/new', methods=['GET', 'POST'])
def new_temporal_feast():
    """Create a new temporal feast."""
    form = TemporalFeastForm()
    if form.validate_on_submit():
        repos = get_repositories()
        feast_data = {
            'id': form.id.data,
            'rank': [form.rank_numeric.data, form.rank_verbose.data],
            'color': form.color.data,
            'office_type': form.office_type.data,
            'nobility': (
                form.nobility_1.data, form.nobility_2.data, form.nobility_3.data,
                form.nobility_4.data, form.nobility_5.data, form.nobility_6.data
            ),
            'mass': json.loads(form.mass_properties.data) if form.mass_properties.data else {},
            'vespers': json.loads(form.vespers_properties.data) if form.vespers_properties.data else {},
            'matins': json.loads(form.matins_properties.data) if form.matins_properties.data else {},
            'lauds': json.loads(form.lauds_properties.data) if form.lauds_properties.data else {},
            'prime': json.loads(form.prime_properties.data) if form.prime_properties.data else {},
            'little_hours': json.loads(form.little_hours_properties.data) if form.little_hours_properties.data else {},
            'compline': json.loads(form.compline_properties.data) if form.compline_properties.data else {},
            'com_1': json.loads(form.com_1_properties.data) if form.com_1_properties.data else {},
            'com_2': json.loads(form.com_2_properties.data) if form.com_2_properties.data else {},
            'com_3': json.loads(form.com_3_properties.data) if form.com_3_properties.data else {},
        }
        try:
            repos['temporal'].save_feast(feast_data)
            flash('Temporal feast created successfully.', 'success')
            return redirect(url_for('browse_data'))
        except Exception as e:
            flash(f'Error saving feast: {str(e)}', 'error')
    
    return render_template('forms/temporal_form.html', form=form, title="New Temporal Feast")


@app.route('/temporal/<feast_id>/edit', methods=['GET', 'POST'])
def edit_temporal_feast(feast_id):
    """Edit an existing temporal feast."""
    repos = get_repositories()
    feast = repos['temporal'].get_feast(feast_id)
    
    if not feast:
        flash('Feast not found.', 'error')
        return redirect(url_for('browse_data'))
    
    form = TemporalFeastForm()
    
    if request.method == 'GET':
        # Populate form
        form.id.data = feast['id']
        form.rank_numeric.data = feast['rank'][0]
        form.rank_verbose.data = feast['rank'][1]
        form.color.data = feast['color']
        form.office_type.data = feast['office_type']
        
        nobility = feast.get('nobility', (None,)*6)
        form.nobility_1.data = nobility[0]
        form.nobility_2.data = nobility[1]
        form.nobility_3.data = nobility[2]
        form.nobility_4.data = nobility[3]
        form.nobility_5.data = nobility[4]
        form.nobility_6.data = nobility[5]
        
        form.mass_properties.data = json.dumps(feast.get('mass', {}), indent=2)
        form.vespers_properties.data = json.dumps(feast.get('vespers', {}), indent=2)
        form.matins_properties.data = json.dumps(feast.get('matins', {}), indent=2)
        form.lauds_properties.data = json.dumps(feast.get('lauds', {}), indent=2)
        form.prime_properties.data = json.dumps(feast.get('prime', {}), indent=2)
        form.little_hours_properties.data = json.dumps(feast.get('little_hours', {}), indent=2)
        form.compline_properties.data = json.dumps(feast.get('compline', {}), indent=2)
        form.com_1_properties.data = json.dumps(feast.get('com_1', {}), indent=2)
        form.com_2_properties.data = json.dumps(feast.get('com_2', {}), indent=2)
        form.com_3_properties.data = json.dumps(feast.get('com_3', {}), indent=2)

    if form.validate_on_submit():
        feast_data = {
            'id': form.id.data,
            'rank': [form.rank_numeric.data, form.rank_verbose.data],
            'color': form.color.data,
            'office_type': form.office_type.data,
            'nobility': (
                form.nobility_1.data, form.nobility_2.data, form.nobility_3.data,
                form.nobility_4.data, form.nobility_5.data, form.nobility_6.data
            ),
            'mass': json.loads(form.mass_properties.data) if form.mass_properties.data else {},
            'vespers': json.loads(form.vespers_properties.data) if form.vespers_properties.data else {},
            'matins': json.loads(form.matins_properties.data) if form.matins_properties.data else {},
            'lauds': json.loads(form.lauds_properties.data) if form.lauds_properties.data else {},
            'prime': json.loads(form.prime_properties.data) if form.prime_properties.data else {},
            'little_hours': json.loads(form.little_hours_properties.data) if form.little_hours_properties.data else {},
            'compline': json.loads(form.compline_properties.data) if form.compline_properties.data else {},
            'com_1': json.loads(form.com_1_properties.data) if form.com_1_properties.data else {},
            'com_2': json.loads(form.com_2_properties.data) if form.com_2_properties.data else {},
            'com_3': json.loads(form.com_3_properties.data) if form.com_3_properties.data else {},
        }
        try:
            repos['temporal'].save_feast(feast_data)
            flash('Temporal feast updated successfully.', 'success')
            return redirect(url_for('browse_data'))
        except Exception as e:
            flash(f'Error saving feast: {str(e)}', 'error')

    return render_template('forms/temporal_form.html', form=form, title="Edit Temporal Feast")


@app.route('/api/sanctoral/feasts')
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

@app.route('/sanctoral/new', methods=['GET', 'POST'])
def new_sanctoral_feast():
    """Create a new sanctoral feast."""
    form = SanctoralFeastForm()
    if form.validate_on_submit():
        repos = get_repositories()
        feast_data = {
            'month': form.month.data,
            'day': form.day.data,
            'diocese_source': form.diocese_source.data if form.diocese_source.data else 'roman',
            'rank': [form.rank_numeric.data, form.rank_verbose.data],
            'color': form.color.data,
            'office_type': form.office_type.data,
            'nobility': (
                form.nobility_1.data, form.nobility_2.data, form.nobility_3.data,
                form.nobility_4.data, form.nobility_5.data, form.nobility_6.data
            ),
            'mass': json.loads(form.mass_properties.data) if form.mass_properties.data else {},
            'vespers': json.loads(form.vespers_properties.data) if form.vespers_properties.data else {},
            'matins': json.loads(form.matins_properties.data) if form.matins_properties.data else {},
            'lauds': json.loads(form.lauds_properties.data) if form.lauds_properties.data else {},
            'prime': json.loads(form.prime_properties.data) if form.prime_properties.data else {},
            'little_hours': json.loads(form.little_hours_properties.data) if form.little_hours_properties.data else {},
            'compline': json.loads(form.compline_properties.data) if form.compline_properties.data else {},
            'com_1': json.loads(form.com_1_properties.data) if form.com_1_properties.data else {},
            'com_2': json.loads(form.com_2_properties.data) if form.com_2_properties.data else {},
            'com_3': json.loads(form.com_3_properties.data) if form.com_3_properties.data else {},
        }
        try:
            repos['sanctoral'].save_feast(feast_data)
            flash('Sanctoral feast created successfully.', 'success')
            return redirect(url_for('browse_data'))
        except Exception as e:
            flash(f'Error saving feast: {str(e)}', 'error')
    
    return render_template('forms/sanctoral_form.html', form=form, title="New Sanctoral Feast")


@app.route('/sanctoral/<int:feast_id>/edit', methods=['GET', 'POST'])
def edit_sanctoral_feast(feast_id):
    """Edit an existing sanctoral feast."""
    repos = get_repositories()
    
    # Try to find the feast (we need to know the diocese to look it up properly if it's unique)
    db = get_db()
    cursor = db.execute("SELECT diocese_id FROM feast_date_assignments WHERE feast_id = ?", (feast_id,))
    assignment = cursor.fetchone()
    
    diocese_code = 'roman'
    if assignment and assignment['diocese_id']:
        d_cursor = db.execute("SELECT code FROM dioceses WHERE id = ?", (assignment['diocese_id'],))
        d_row = d_cursor.fetchone()
        if d_row:
            diocese_code = d_row['code']
            
    feast = repos['sanctoral'].get_feast(feast_id, diocese_code if diocese_code != 'roman' else None)
    
    if not feast:
        flash('Feast not found.', 'error')
        return redirect(url_for('browse_data'))
        
    # Get date assignment
    cursor = db.execute("SELECT month, day FROM feast_date_assignments WHERE feast_id = ?", (feast_id,))
    date_row = cursor.fetchone()
    
    form = SanctoralFeastForm()
    
    if request.method == 'GET':
        # Populate form
        form.id.data = feast['id']
        form.month.data = date_row['month'] if date_row else None
        form.day.data = date_row['day'] if date_row else None
        form.diocese_source.data = diocese_code
        
        form.rank_numeric.data = feast['rank'][0]
        form.rank_verbose.data = feast['rank'][1]
        form.color.data = feast['color']
        form.office_type.data = feast['office_type']
        
        nobility = feast.get('nobility', (None,)*6)
        form.nobility_1.data = nobility[0]
        form.nobility_2.data = nobility[1]
        form.nobility_3.data = nobility[2]
        form.nobility_4.data = nobility[3]
        form.nobility_5.data = nobility[4]
        form.nobility_6.data = nobility[5]
        
        form.mass_properties.data = json.dumps(feast.get('mass', {}), indent=2)
        form.vespers_properties.data = json.dumps(feast.get('vespers', {}), indent=2)
        form.matins_properties.data = json.dumps(feast.get('matins', {}), indent=2)
        form.lauds_properties.data = json.dumps(feast.get('lauds', {}), indent=2)
        form.prime_properties.data = json.dumps(feast.get('prime', {}), indent=2)
        form.little_hours_properties.data = json.dumps(feast.get('little_hours', {}), indent=2)
        form.compline_properties.data = json.dumps(feast.get('compline', {}), indent=2)
        form.com_1_properties.data = json.dumps(feast.get('com_1', {}), indent=2)
        form.com_2_properties.data = json.dumps(feast.get('com_2', {}), indent=2)
        form.com_3_properties.data = json.dumps(feast.get('com_3', {}), indent=2)

    if form.validate_on_submit():
        feast_data = {
            'id': feast_id,
            'month': form.month.data,
            'day': form.day.data,
            'diocese_source': form.diocese_source.data if form.diocese_source.data else 'roman',
            'rank': [form.rank_numeric.data, form.rank_verbose.data],
            'color': form.color.data,
            'office_type': form.office_type.data,
            'nobility': (
                form.nobility_1.data, form.nobility_2.data, form.nobility_3.data,
                form.nobility_4.data, form.nobility_5.data, form.nobility_6.data
            ),
            'mass': json.loads(form.mass_properties.data) if form.mass_properties.data else {},
            'vespers': json.loads(form.vespers_properties.data) if form.vespers_properties.data else {},
            'matins': json.loads(form.matins_properties.data) if form.matins_properties.data else {},
            'lauds': json.loads(form.lauds_properties.data) if form.lauds_properties.data else {},
            'prime': json.loads(form.prime_properties.data) if form.prime_properties.data else {},
            'little_hours': json.loads(form.little_hours_properties.data) if form.little_hours_properties.data else {},
            'compline': json.loads(form.compline_properties.data) if form.compline_properties.data else {},
            'com_1': json.loads(form.com_1_properties.data) if form.com_1_properties.data else {},
            'com_2': json.loads(form.com_2_properties.data) if form.com_2_properties.data else {},
            'com_3': json.loads(form.com_3_properties.data) if form.com_3_properties.data else {},
        }
        try:
            repos['sanctoral'].save_feast(feast_data)
            flash('Sanctoral feast updated successfully.', 'success')
            return redirect(url_for('browse_data'))
        except Exception as e:
            flash(f'Error saving feast: {str(e)}', 'error')

    return render_template('forms/sanctoral_form.html', form=form, title="Edit Sanctoral Feast")



@app.route('/temporal/<feast_id>/delete', methods=['POST'])
def delete_temporal_feast(feast_id):
    """Delete a temporal feast."""
    repos = get_repositories()
    try:
        repos['temporal'].delete_feast(feast_id)
        flash('Temporal feast deleted successfully.', 'success')
    except Exception as e:
        flash(f'Error deleting feast: {str(e)}', 'error')
    return redirect(url_for('browse_data'))


@app.route('/sanctoral/<int:feast_id>/delete', methods=['POST'])
def delete_sanctoral_feast(feast_id):
    """Delete a sanctoral feast."""
    repos = get_repositories()
    try:
        repos['sanctoral'].delete_feast(feast_id)
        flash('Sanctoral feast deleted successfully.', 'success')
    except Exception as e:
        flash(f'Error deleting feast: {str(e)}', 'error')
    return redirect(url_for('browse_data'))


@app.route('/browse')
def browse_data():
    """Browse all data in the database."""
    return render_template('browse.html')


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
