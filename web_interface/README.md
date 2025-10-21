# Ordotools Web Interface

A simple web interface using HTMX to manage the Ordotools liturgical database.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Features

- Database connection testing
- View database statistics
- **Browse all data** with pagination and filtering
- View recent entries by diocese and year
- Filter by diocese and year
- API endpoints for querying feasts, dioceses, and years

## Pages

- `/` - Main dashboard with connection testing
- `/browse` - Browse all database records with filters and pagination

## API Endpoints

- `GET /` - Main web interface
- `GET /browse` - Browse data interface
- `GET /api/test-connection` - Test database connectivity
- `GET /api/browse/feasts?page=1&diocese=X&year=Y` - Browse feasts with pagination and filters
- `GET /api/feasts?diocese=X&year=Y` - Get feasts (with optional filters)
- `GET /api/dioceses` - Get list of dioceses
- `GET /api/years` - Get list of years

## Next Steps

Forms for adding, editing, and deleting feast entries will be implemented in the next phase.

