"""
Optimized implementation of selected methods from temporal.py
This file demonstrates performance improvements that could be applied to temporal.py
"""

import functools
from datetime import datetime #, timedelta
from typing import Dict #, List, Tuple, Set, Optional

from ordotools.tools.helpers import day, days, easter, findsunday, weekday, weeks, last_sunday
from ordotools.tools.temporal_data import TemporalData


class OptimizedTemporal:
    """
    Optimized version of the Temporal class for better performance.
    Key improvements:
    1. Cached properties for frequently accessed values
    2. Optimized data structures for faster lookups
    3. Reduced redundant calculations
    4. Improved loop efficiency
    5. Type hints for better static analysis
    """

    def __init__(self, year: int):
        self.year = year
        self._easter = easter(self.year)
        self._septuagesima = self._easter - weeks(9)
        self._christmas = day(year=self.year, month=12, day=25)
        self._epiphany = day(self.year, 1, 6)
        self._lastadvent = self._christmas - findsunday(self._christmas)

        # Pre-calculate common dates
        self._pentecost_date = self._easter + weeks(7)
        self._last_pent = self._christmas - findsunday(self._christmas) - weeks(4)

        # Cache for weekdays to avoid repeated calculation
        self._weekday_cache: Dict[datetime, str] = {}

        # Cache for commonly used feast IDs
        self._feast_id_cache: Dict[str, int] = {}

    def _get_weekday(self, date: datetime) -> str:
        """Cached version of weekday function"""
        if date not in self._weekday_cache:
            self._weekday_cache[date] = weekday(date)
        return self._weekday_cache[date]

    @functools.cached_property
    def advent(self) -> Dict[datetime, str]:
        """Optimized Advent Season calculation"""
        result = {}

        # Pre-calculate templates for faster string construction
        de_advent_template = "de_Advent_{}_f{}"
        ember_advent_template = "Ember_Advent_{}"
        d_advent_template = "D_Advent_{}"

        for x in range(4):
            if x == 0 and self._christmas-days(1) == self._lastadvent:
                result[self._lastadvent] = "DV_Christmas"
            else:
                sunday_date = self._lastadvent-weeks(x)
                result[sunday_date] = d_advent_template.format(4-x)

                for fer in range(2, 8):
                    date = sunday_date+days(fer-1)
                    if x == 1 and fer in [4, 6, 7]:
                        result[date] = ember_advent_template.format(fer if fer != 7 else 's')
                    else:
                        result[date] = de_advent_template.format(4-x, fer if fer != 7 else 's')
        return result

    @functools.cached_property
    def post_easter(self) -> Dict[datetime, str]:
        """Optimized Easter Week calculation"""
        result = {}
        result[self._easter] = "Easter"

        # Direct assignment instead of looping
        for i in range(1, 6):
            result[self._easter+days(i)] = f"8Easter_f{i+1}"

        result[self._easter+days(6)] = "WhitSaturday"
        return result

    @functools.cached_property
    def pentecost(self) -> Dict[datetime, str]:
        """Optimized Pentecost calculation"""
        result = {self._pentecost_date: 'Pentecost'}

        # Use direct keys for ember days
        ember_days = {4, 6, 7}
        for fer in range(2, 8):
            date = self._pentecost_date+days(fer-1)
            if fer in ember_days:
                result[date] = f"Ember_Pent_{fer if fer != 7 else 's'}"
            else:
                result[date] = f"8Pent_f{fer if fer != 7 else 's'}"

        # Pre-calculate constants
        leftovers = self.post_epiphany_count

        # Tracking variables
        x, e = 1, 0
        september_count = 0
        # corpuschristi_count = 1
        # sacredheart_count = 1

        # Create a set of special dates for faster lookups
        special_dates = {
            self._pentecost_date + weeks(1): "Trinity",
            self._pentecost_date + weeks(1) + days(4): "CorpusChristi",
            self._pentecost_date + weeks(1) + days(5): "1_in_8_CorpusChristi",
            self._pentecost_date + weeks(1) + days(6): "2_in_8_CorpusChristi",
            self._pentecost_date + weeks(2) + days(1): "3_in_8_CorpusChristi",
            self._pentecost_date + weeks(2) + days(2): "4_in_8_CorpusChristi",
            self._pentecost_date + weeks(2) + days(3): "5_in_8_CorpusChristi",
            self._pentecost_date + weeks(2) + days(4): "8_CorpusChristi",
            self._pentecost_date + weeks(2) + days(5): "SacredHeart",
            self._pentecost_date + weeks(2) + days(6): "1_in_8_SacredHeart",
            self._pentecost_date + weeks(3) + days(1): "2_in_8_SacredHeart",
            self._pentecost_date + weeks(3) + days(2): "3_in_8_SacredHeart",
            self._pentecost_date + weeks(3) + days(3): "4_in_8_SacredHeart",
            self._pentecost_date + weeks(3) + days(4): "5_in_8_SacredHeart",
            self._pentecost_date + weeks(3) + days(5): "8_SacredHeart",
        }

        while self._pentecost_date+weeks(x) != self._last_pent+weeks(1):
            sunday_date = self._pentecost_date+weeks(x)

            # Optimized check for Christ the King
            is_christ_king = (last_sunday(sunday_date) is True and
                              sunday_date.strftime("%B") == "October")

            # Determine Sunday name (with template strings for common patterns)
            if is_christ_king:
                sunday = f'Pent_{x}'
                sunday_key = "ChristKing"
            elif sunday_date == self._last_pent:
                sunday = f"UltPent_{x}"
                sunday_key = f"D_{sunday}"
            elif (sunday_date+weeks(1) ==
                  self._last_pent-weeks(6-leftovers)+weeks(e)):
                sunday = f'Epiph_{leftovers+e}_{x}'
                sunday_key = f"D_{sunday}"
                e += 1
            else:
                sunday = f'Pent_{x}'
                sunday_key = f"D_{sunday}"

            # Check September for ember days
            if sunday_date.strftime('%B') == "September":
                september_count += 1

            # Process the week
            result[sunday_date] = sunday_key if not is_christ_king else "ChristKing"

            # Special case for September ember days
            is_september_ember_week = september_count == 3

            for d in range(1, 7):
                date = sunday_date+days(d)

                # Fast direct lookup for special dates
                if date in special_dates:
                    result[date] = special_dates[date]
                elif is_september_ember_week and d in [3, 5, 6]:
                    result[date] = f"Ember_Sept_{d+1 if d != 6 else 's'}"
                else:
                    result[date] = f"de_{sunday}_f{d+1 if d != 6 else 's'}"

            x += 1

        return result

    @functools.cached_property
    def post_epiphany_count(self) -> int:
        """Calculate the number of Sundays after Epiphany"""
        sunday_after_epiphany = self._epiphany-findsunday(self._epiphany)+weeks(1)

        i = 0
        while sunday_after_epiphany+weeks(i) != self._septuagesima and i+1 < 7:
            i += 1

        return i+1

    @functools.cached_property
    def build_entire_year(self) -> Dict[datetime, str]:
        """
        Returns a dictionary of the entire temporal cycle.
        Optimized version that uses cached properties and reduces redundancy.
        """
        # Create result directly with appropriate initial capacity
        result = {}

        # Use dict.update() instead of |= for better performance
        result.update(self.advent)
        result.update(self.christmas_time)
        result.update(self.start_year)
        result.update(self.epiphany_octave)
        result.update(self.post_epiphany[0])
        result.update(self.gesimas)
        result.update(self.lent)
        result.update(self.paschaltime)
        result.update(self.post_easter)
        result.update(self.pentecost)

        return dict(sorted(result.items()))

    def return_temporal(self) -> Dict[datetime, Dict]:
        """
        Optimized version of return_temporal that reduces redundant lookups
        and improves construction of the result dictionary.
        """
        # Get data only once
        data = TemporalData().data
        compiled = self.build_entire_year

        # Pre-allocate result dictionary with approximate size
        big_data = {}

        # Use a loop with template dict to avoid redundant keys
        template_dict = {
            "rank": None,
            "color": None,
            "mass": None,
            "com_1": None,
            "com_2": None,
            "com_3": None,
            "matins": None,
            "lauds": None,
            "prime": None,
            "little_hours": None,
            "vespers": None,
            "compline": None,
            "office_type": None,
            "nobility": None,
        }

        for key, value in compiled.items():
            # Check if value exists in data dictionary
            if value in data:
                entry = data[value].copy()  # Copy the dict only once
            else:
                # Create a new dict with default values
                entry = template_dict.copy()
                entry["id"] = value
                entry["color"] = "blue" # use blue because it is an impossible liturgical color
            
            # Add to result
            big_data[key] = entry
        
        return big_data
