# Ordotools Documentation

## Commands
- **Run application**: `python3 run.py`
- **Run tests**: `pytest`
- **Run single test**: `pytest tests/test_.py::test_basic`
- **Run performance test**: `pytest tests/test_.py::test_performance`
- **Run detailed benchmark**: `./benchmark.py --years 2025,2026 --runs 5 --dioceses roman`
- **Setup environment**: `python3 -m venv env && source env/bin/activate && pip install -r requirements.txt`
- **Install package**: `pip install -e .`

## Project Overview
Ordotools is a Python library for generating traditional Catholic liturgical calendars (Ordo). It calculates feasts, commemorations, and liturgical seasons according to the traditional Roman Catholic calendar. The library determines proper feasts, commemorations, ranks, and liturgical colors for each day throughout the liturgical year.

## Core Components

### LiturgicalCalendar (main.py)
The main class that orchestrates calendar generation by combining:
- Temporal cycle (moveable feasts)
- Sanctoral cycle (fixed feasts)
- Commemorations, octaves, and fasting days

#### Key Methods:
- `build()`: Generates the complete liturgical year calendar
- `add_feasts()`: Combines temporal and sanctoral cycles
- `find_octave()`: Processes octaves for major feasts
- `our_ladys_saturday()`: Implements Saturday Office of the Blessed Virgin

### Feast (feast.py)
Represents a single day in the liturgical calendar with properties for:
- Name, date, and rank of the feast
- Liturgical color
- Commemorations
- Office details (Matins, Lauds, Vespers, etc.)
- Fasting/abstinence status

### Rank System (rank.py)
Resolves conflicts between feasts occurring on the same day:
- Lower numerical ranks have higher precedence (e.g. rank 2 > rank 10)
- Complex precedence matrix determines which feast takes precedence
- "Nobility" tuple provides finer ranking between feasts of same rank
- Handles commemorations when feasts are displaced

### Temporal (temporal.py)
Handles the moveable feast cycle based on Easter date:
- Calculates dates for Advent, Christmas, Epiphany, Septuagesima, Lent, Easter, Ascension, Pentecost
- Assigns proper ranks and colors to these feasts

### Sanctoral
Calendar data for fixed feasts organized by:
- Roman calendar (universal calendar)
- Diocesan calendars (local feast days)
- Country-specific collections

## Data Structure
Feast ranking system uses numerical values (2-23):
- 2: Duplex I classis (highest)
- 10: Duplex II classis
- 13: Dies Octava Communis
- 15: Duplex minus
- 16: Semiduplex
- 22: Simplex (lowest regular feast)
- 23: Feria (ordinary weekday)

## Usage Examples

### Basic Calendar Generation
```python
from ordotools import LiturgicalCalendar

# Create calendar for 2025 using Roman diocese and Latin language
calendar = LiturgicalCalendar(2025, "roman", "la").build()

# Print basic information for each feast
for feast in calendar:
    print(feast.date, feast.name, feast.rank_v, feast.color)
```

### Creating a Custom Diocesan Calendar
To create a new diocesan calendar:
1. Copy `sanctoral/diocese/_TEMPLATE.py` to a new file (e.g. `mydiocese.py`)
2. Implement the `Diocese` class with your diocesan feasts
3. Use the calendar with: `LiturgicalCalendar(2025, "mydiocese", "la").build()`

## Code Style
- **Imports**: Standard library first, then third-party, then local modules
- **Formatting**: 4-space indentation, max line length ~80 characters
- **Naming**: snake_case for functions/variables, CamelCase for classes
- **Documentation**: Docstrings for public functions and classes
- **Error handling**: Use appropriate exception handling with descriptive messages
- **Type hints**: Not currently used but encouraged for new code
- **Logging**: Use the built-in logger module for important events

## Project Structure
- Core functionality in `ordotools/tools/`
- Calendar data in `ordotools/sanctoral/`
- New calendar implementations should follow templates in relevant directories

## Project Status
The project is in late alpha development with some known inaccuracies. Ongoing work focuses on improving accuracy and completeness of the calendar generation.

## Testing and Performance Benchmarking

### Testing Framework
The project uses pytest for testing, with tests organized in the `tests/` directory:
- Basic instantiation tests ensure calendar generation works for all years
- Calendar type tests validate different diocesan calendars
- Country module tests verify proper module loading

### Performance Testing
Performance testing is built into the test suite to track calendar generation speed:

1. **Simple Performance Test** (`pytest tests/test_.py::test_performance`)
   - Measures average runtime for calendar generation across multiple years
   - Compares current performance with previous runs
   - Records performance metrics in `tests/performance_history.json`
   - Reports percentage improvement or regression
   - Shows historical performance trend

2. **Comprehensive Benchmark** (`./benchmark.py`)
   - Command-line tool for detailed performance analysis
   - Parameters:
     - `--years`: Comma-separated list of years to test (default: 2025,2026,2027)
     - `--runs`: Number of runs per test for statistical significance (default: 5)
     - `--dioceses`: Comma-separated list of dioceses to test (default: roman)
   - Features:
     - Calculates average runtime and standard deviation
     - Compares with historical performance 
     - Visualizes performance trends with matplotlib
     - Saves benchmark data to `benchmark_history.json`
     - Generates performance trend graph in `performance_trend.png`

3. **Profiling Tool** (`profiledRun.py`)
   - Python's cProfile-based profiling 
   - Identifies hotspots and bottlenecks in the code
   - Sorted by cumulative time to find optimization targets

### Interpreting Performance Results
- **Build time**: Average seconds to generate a complete liturgical calendar
- **Trend**: Percentage change from previous performance measurements
- **Historical best**: Comparison with fastest recorded run
- **Standard deviation**: Variation between runs (lower is better)

When optimizing, focus on areas identified in the Performance Optimization Notes section.

## Performance Optimization Notes

### Temporal.py Optimization
The temporal.py module handles calculating all moveable feasts and can be optimized for improved performance:

1. **Use cached properties for commonly accessed values**
   - Add caching for the return values of methods like `build_entire_year()`
   - Convert commonly called methods to properties with functools.cached_property

2. **Replace dictionary merging**
   - Replace the `|=` dictionary merge operator with traditional dictionary operations
   - Use dict.update() instead of |= for older Python versions or better performance

3. **Optimize date calculations**
   - Pre-calculate and store common date references (like pentecost_date, last_pent)
   - Reduce redundant datetime calculations by storing intermediate values

4. **Replace string concatenation in loops**
   - Avoid f-string formatting in tight loops
   - Use predefined templates instead of dynamic string construction

5. **Optimize loops with early termination**
   - Add break conditions for loops with known endings
   - Combine nested loops where possible

6. **Memoize helper functions**
   - Add LRU caching to frequently called helper functions in helpers.py
   - Cache repeated calculations like weekday(), findsunday()

7. **Optimize data structure lookups**
   - Replace linear searches with direct lookups
   - Use sets for membership testing instead of lists

8. **Type hint optimization**
   - Add type hints to enable better static analysis and optimization
   - Helps with JIT compilation and runtime efficiency

Implementation of these optimizations should significantly improve performance of calendar generation, especially for large batches of years or multiple concurrent calendars.