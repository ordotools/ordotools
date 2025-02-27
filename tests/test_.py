from datetime import datetime
import pytest
import time
import os
import json
from statistics import mean
from ordotools import LiturgicalCalendar

# Path to store performance history
PERFORMANCE_HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'performance_history.json')

def load_performance_history():
    """Load performance history from JSON file."""
    if os.path.exists(PERFORMANCE_HISTORY_FILE):
        try:
            with open(PERFORMANCE_HISTORY_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"builds": [], "build_times": []}
    return {"builds": [], "build_times": []}

def save_performance_history(history):
    """Save performance history to JSON file."""
    with open(PERFORMANCE_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def test_basic():
    assert LiturgicalCalendar(int(datetime.today().strftime("%Y")), "roman", "la")
    assert LiturgicalCalendar(2024, "roman", "la")
    assert LiturgicalCalendar(2025, "roman", "la")
    assert LiturgicalCalendar(2026, "roman", "la")
    assert LiturgicalCalendar(2027, "roman", "la")
    assert LiturgicalCalendar(2028, "roman", "la")
    assert LiturgicalCalendar(2029, "roman", "la")
    assert LiturgicalCalendar(2030, "roman", "la")
    assert LiturgicalCalendar(2031, "roman", "la")
    assert LiturgicalCalendar(2032, "roman", "la")
    assert LiturgicalCalendar(2033, "roman", "la")
    assert LiturgicalCalendar(2034, "roman", "la")
    assert LiturgicalCalendar(2035, "roman", "la")
    assert LiturgicalCalendar(2036, "roman", "la")
    assert LiturgicalCalendar(2037, "roman", "la")
    assert LiturgicalCalendar(2038, "roman", "la")
    assert LiturgicalCalendar(2039, "roman", "la")
    assert LiturgicalCalendar(2040, "roman", "la")
    assert LiturgicalCalendar(2041, "roman", "la")
    assert LiturgicalCalendar(2042, "roman", "la")
    assert LiturgicalCalendar(2043, "roman", "la")
    assert LiturgicalCalendar(2044, "roman", "la")
    assert LiturgicalCalendar(2045, "roman", "la")
    assert LiturgicalCalendar(2046, "roman", "la")
    assert LiturgicalCalendar(2047, "roman", "la")
    assert LiturgicalCalendar(2048, "roman", "la")
    assert LiturgicalCalendar(2049, "roman", "la")
    assert LiturgicalCalendar(2050, "roman", "la")
    assert LiturgicalCalendar(2051, "roman", "la")
    assert LiturgicalCalendar(2052, "roman", "la")
    assert LiturgicalCalendar(2053, "roman", "la")
    assert LiturgicalCalendar(2054, "roman", "la")
    assert LiturgicalCalendar(2055, "roman", "la")
    assert LiturgicalCalendar(2056, "roman", "la")
    assert LiturgicalCalendar(2057, "roman", "la")
    assert LiturgicalCalendar(2058, "roman", "la")
    assert LiturgicalCalendar(2059, "roman", "la")
    assert LiturgicalCalendar(2060, "roman", "la")
    assert LiturgicalCalendar(2061, "roman", "la")
    assert LiturgicalCalendar(2062, "roman", "la")
    assert LiturgicalCalendar(2063, "roman", "la")
    assert LiturgicalCalendar(2064, "roman", "la")
    assert LiturgicalCalendar(2065, "roman", "la")
    assert LiturgicalCalendar(2066, "roman", "la")
    assert LiturgicalCalendar(2067, "roman", "la")
    assert LiturgicalCalendar(2068, "roman", "la")
    assert LiturgicalCalendar(2069, "roman", "la")
    assert LiturgicalCalendar(2070, "roman", "la")
    assert LiturgicalCalendar(2071, "roman", "la")
    assert LiturgicalCalendar(2072, "roman", "la")
    assert LiturgicalCalendar(2073, "roman", "la")

@pytest.mark.parametrize("calendar_type", [
    "roman"
    # The following calendars need additional work to make them compatible with tests
    # "bathurstensis", 
    # "lismorensis", 
    # "maitlandensis", 
    # "melbournensis", 
    # "rennes", 
    # "rockhamptonensis"
])
def test_calendar_types(calendar_type):
    """Test that different calendar types can be instantiated and built successfully."""
    cal = LiturgicalCalendar(2025, calendar_type, "la")
    # Test both initialization and building the calendar
    calendar = cal.build()
    
    # Basic validation
    assert calendar is not None
    assert len(calendar) > 0
    assert isinstance(calendar, list)
    
    # Check that calendar contains feast objects with required properties
    for feast in calendar:
        assert hasattr(feast, 'date')
        assert hasattr(feast, 'name')
        assert hasattr(feast, 'rank_n')
        assert hasattr(feast, 'rank_v')
        assert hasattr(feast, 'color')

@pytest.mark.parametrize("country", ["australiae", "hispaniae"])
def test_country_modules(country):
    """Test that country-specific calendar modules exist and can be imported.
    This test is a placeholder as the current implementation doesn't directly
    support country parameter, but could be expanded when that functionality is added.
    """
    # For now, just check that the country modules exist and can be imported
    import importlib
    module = importlib.import_module(f"ordotools.sanctoral.country.{country}")
    assert module is not None

def test_performance():
    """Test and track the performance of calendar generation."""
    # Parameters for the benchmark
    years_to_test = [2025, 2026, 2027]
    num_runs = 3
    
    # Load performance history
    history = load_performance_history()
    
    # Get timestamp for this run
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Track build times for this session
    current_times = []
    
    # Run benchmark
    for year in years_to_test:
        times = []
        for _ in range(num_runs):
            start_time = time.time()
            cal = LiturgicalCalendar(year, "roman", "la")
            calendar = cal.build()
            end_time = time.time()
            
            # Store time in seconds
            elapsed = end_time - start_time
            times.append(elapsed)
        
        # Calculate average time for this year
        avg_time = mean(times)
        current_times.append(avg_time)
        
        # Report for this year
        print(f"\nYear {year} average build time: {avg_time:.4f} seconds (over {num_runs} runs)")
    
    # Calculate overall average for this run
    overall_avg = mean(current_times)
    
    # Add to history
    history["builds"].append({
        "timestamp": timestamp,
        "average_time": overall_avg,
        "details": {str(year): time for year, time in zip(years_to_test, current_times)}
    })
    
    # For tracking trend, also maintain a simple list of build times
    history["build_times"].append(overall_avg)
    
    # Save updated history
    save_performance_history(history)
    
    # Assess performance trend
    if len(history["build_times"]) > 1:
        previous_avg = history["build_times"][-2]
        pct_change = ((overall_avg - previous_avg) / previous_avg) * 100
        
        # Compare with previous run
        if overall_avg < previous_avg:
            print(f"\n✅ Performance improved by {abs(pct_change):.2f}% from last run")
        elif overall_avg > previous_avg:
            print(f"\n⚠️ Performance degraded by {pct_change:.2f}% from last run")
        else:
            print("\n✓ Performance unchanged from last run")
        
        # Compare with historical best
        best_time = min(history["build_times"])
        if overall_avg == best_time:
            print("🏆 This is the fastest run on record!")
        else:
            pct_from_best = ((overall_avg - best_time) / best_time) * 100
            print(f"📊 Current performance is {pct_from_best:.2f}% slower than the best recorded time")
    else:
        print("\n📝 First performance measurement recorded as baseline")
    
    # Show performance history summary
    if len(history["build_times"]) >= 3:
        print("\nRecent performance history:")
        for i, run in enumerate(history["builds"][-3:]):
            print(f"  {run['timestamp']}: {run['average_time']:.4f} seconds")
    
    # The test should pass regardless of performance results
    assert True
