#!/usr/bin/env python3
"""
Simple Flask web interface with HTMX for managing ordotools database.
"""

import sys
import os

# Add parent directory to path to import ordotools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, jsonify, request, g
from ordotools.tools.db import get_connection
from ordotools.tools.repositories.dioceses_repo import DiocesesRepository
from ordotools.tools.repositories.temporal_repo import TemporalRepository
from ordotools.tools.repositories.sanctoral_repo import SanctoralRepository
from ordotools.tools.repositories.translations_repo import TranslationsRepository
import json

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


@app.route('/')
def index():
    """Main page with HTMX interface."""
    return render_template('index.html')


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
def get_countries():
    """Get all countries."""
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


@app.route('/api/dioceses')
def get_dioceses_api():
    """Get all dioceses."""
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


@app.route('/api/temporal/feasts')
def get_temporal_feasts():
    """Get temporal feasts."""
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


@app.route('/api/sanctoral/feasts')
def get_sanctoral_feasts():
    """Get sanctoral feasts for a diocese and date."""
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

