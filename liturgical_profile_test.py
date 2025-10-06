
from ordotools import LiturgicalCalendar
import time

print("🗓️  Starting liturgical calendar profiling...")

# Test different scenarios
scenarios = [
    (2024, "roman", "la"),
    (2025, "roman", "la"),
    (2026, "roman", "la"),
]

for year, rite, language in scenarios:
    print(f"📅 Building calendar for {year} ({rite}, {language})...")
    start_time = time.time()
    
    cal = LiturgicalCalendar(year, rite, language)
    data = cal.build()
    
    end_time = time.time()
    entry_count = len(data) if hasattr(data, '__len__') else 'N/A'
    
    print(f"✅ {year}: {entry_count} entries in {end_time - start_time:.3f}s")
    
    # Small delay to see the pattern in profiler
    time.sleep(0.1)

print("🏁 Profiling complete!")
