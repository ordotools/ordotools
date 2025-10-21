# Quick Start Guide

## Starting the Web Interface

### Option 1: Using the startup script
```bash
cd web_interface
./start.sh
```

### Option 2: Manual start
```bash
cd web_interface
source ../env/bin/activate
python app.py
```

## Accessing the Interface

Once started, open your browser to:
```
http://127.0.0.1:5000
```

## What's Working

- ✅ Database connection to `ordotools.sqlite3`
- ✅ Modern, responsive UI with HTMX
- ✅ New database schema with separate temporal/sanctoral tables
- ✅ Connection testing interface with full statistics
- ✅ Browse temporal feasts (744 feasts)
- ✅ Browse sanctoral feasts by diocese (271 feasts)
- ✅ Countries and dioceses management
- ✅ Repository-based data access

## Current Database Contents

The database contains:
- **744 temporal feasts** - Liturgical feasts based on the calendar cycle
- **271 sanctoral feasts** - Saint feast days and memorials
- **7 dioceses** - Roman and local dioceses (Australia, Spain)
- **2 countries** - Organizational hierarchy
- **2,393 translations** - Multi-language support for feast names

## API Endpoints

### Database Status
- `GET /api/test-connection` - Test connection and get statistics

### Countries & Dioceses
- `GET /api/countries` - List all countries
- `GET /api/dioceses` - List all dioceses
- `GET /api/dioceses?country=CODE` - Get dioceses by country

### Feasts
- `GET /api/temporal/feasts?limit=N` - Get temporal feasts
- `GET /api/sanctoral/feasts?diocese=CODE&month=M&day=D` - Get sanctoral feasts
- `GET /api/browse/temporal?page=N&per_page=N&language=LANG` - Browse temporal feasts (paginated with translations)
- `GET /api/browse/sanctoral?page=N&per_page=N&diocese=CODE&language=LANG&unique_only=true/false` - Browse sanctoral feasts (paginated with translations and filtering)

### Browse Endpoints
- `GET /api/browse/dioceses?page=N&per_page=N` - Browse dioceses (paginated)
- `GET /api/browse/countries?page=N&per_page=N` - Browse countries (paginated)
- `GET /api/browse/translations?page=N&per_page=N&feast_type=TYPE&language=LANG` - Browse translations (paginated with filtering)

### Utility Endpoints
- `GET /api/languages` - Get list of available language codes

## Browse Interface

The browse page (`/browse`) provides comprehensive access to all database tables with the following features:

### 📅 Temporal Feasts Tab
- Browse all 744 temporal feasts
- Select language for feast names (Latin, English, French)
- View feast rank, color, and office type
- Color-coded rank badges (1st class, 2nd class, etc.)

### ⛪ Sanctoral Feasts Tab
- Browse sanctoral feasts by diocese
- **Unique to diocese** checkbox - shows only feasts specific to that diocese (excludes Roman feasts)
- Select language for feast names
- Source indicator showing which diocese the feast comes from (Roman or local)
- Color-coded rank and liturgical color badges
- Filter by: diocese, language, and uniqueness

### 🏛️ Dioceses Tab
- Browse all dioceses with their Latin and English names
- Shows associated country for each diocese
- Displays universal (Roman) vs local dioceses

### 🌍 Countries Tab
- View all countries with Latin and English names
- See organizational hierarchy for dioceses

### 🌐 Translations Tab
- Browse all feast name translations
- Filter by feast type (temporal/sanctoral)
- Filter by language code
- Shows which translation is marked as default (Latin)
- Access to all 2,393 translations in the database

## Next Steps

Future enhancements:
- Translation viewer and editor
- Add new feast entries via forms
- Edit existing entries
- Advanced search and filtering
- Bulk import/export operations

## Stopping the Server

Press `Ctrl+C` in the terminal to stop the Flask server.

