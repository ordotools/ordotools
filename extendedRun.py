# extended_run.py - Modified version of your run.py for better profiling

from ordotools import LiturgicalCalendar
import time

def profile_multiple_years():
    """Run your calendar generation multiple times for better profiling"""
    print("Starting extended profiling run...")
    
    years = [2024, 2025, 2026, 2027, 2028]
    languages = ["la", "en"]  # Add more if you support them
    rites = ["roman"]
    
    total_start = time.time()
    
    for iteration in range(3):  # Run 3 iterations
        print(f"\n=== Iteration {iteration + 1} ===")
        
        for year in years:
            for lang in languages:
                for rite in rites:
                    print(f"Building calendar: {year}, {rite}, {lang}")
                    
                    start_time = time.time()
                    
                    # This is your actual code being profiled
                    cal = LiturgicalCalendar(year, rite, lang)
                    data = cal.build()
                    
                    end_time = time.time()
                    elapsed = end_time - start_time
                    
                    entry_count = len(data) if hasattr(data, '__len__') else 'N/A'
                    print(f"  -> {entry_count} entries in {elapsed:.3f}s")
                    
                    # Small delay to make the pattern visible in flame graph
                    time.sleep(0.01)
    
    total_time = time.time() - total_start
    print(f"\nTotal profiling time: {total_time:.2f} seconds")
    print("Profiling complete!")

if __name__ == "__main__":
    profile_multiple_years()

