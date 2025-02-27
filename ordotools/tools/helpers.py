from datetime import datetime
from datetime import timedelta

import dateutil.easter
import re
import functools


@functools.lru_cache(maxsize=128)
def findsunday(date: datetime) -> timedelta:
    """
    return the distance betweent the date and
    the previous Sunday, as timedelta.days
    """
    return timedelta(days=int(date.strftime('%w')))


@functools.lru_cache(maxsize=128)
def easter(year: int) -> datetime:
    """ return the date of easter for this year """
    easter_date = dateutil.easter.easter(year)
    return datetime(
        year=easter_date.year,
        month=easter_date.month,
        day=easter_date.day
    )


class LiturgicalYearMarks:
    _instances = {}  # Class-level cache for instances
    
    def __new__(cls, year):
        # Use existing instance from cache if available
        if year in cls._instances:
            return cls._instances[year]
        
        # Create new instance
        instance = super(LiturgicalYearMarks, cls).__new__(cls)
        cls._instances[year] = instance
        return instance

    def __init__(self, year):
        # Skip initialization if already initialized
        if hasattr(self, 'year') and self.year == year:
            return
            
        self.year = year
        self.christmas = datetime(year=self.year, month=12, day=25)
        
        # Pre-calculate common date references
        self._easter_date = easter(self.year)
        sunday_offset = findsunday(self.christmas)
        
        self.first_advent = self.christmas - sunday_offset - timedelta(weeks=3)
        self.last_advent = self.christmas - timedelta(days=1)

        # Ash Wednesday:
        self.lent_begins = self._easter_date - timedelta(weeks=6, days=4)
        # Holy Saturday:
        self.lent_ends = self._easter_date - timedelta(days=1)

        self.easter = self._easter_date
        self.easter_season_start = self._easter_date
        self.easter_season_end = self._easter_date + timedelta(days=39)
        self.pentecost_season_start = self._easter_date + timedelta(days=49)
        self.pentecost_season_end = self.first_advent - timedelta(days=1)


ladys_office = {
    "id": "lady_saturday",
    "rank": [21, "s"],
    "color": "white",
    "mass": {
        "int": "Salve sancta parens",
        "glo": True,
        "cre": False,
        "pre": "de B Maria Virg (et te in Veneratione)"
    },
    "com_1": {"oration": "Deus qui corda"},
    "com_2": {"oration": "Ecclesiæ"},
    "com_3": {},
    "matins": {},
    "lauds": {},
    "prime": {"responsory": "Qui natus est", "preces": True},
    "little_hours": {},
    "vespers": {
        "proper": False,
        "admag": ("firstVespers", "secondVespers"),
        "propers": {},
        "oration": ""
    },
    "compline": {},
    "office_type": "ut in pr loco",
    "nobility": (8, 2, 6, 13, 3, 0,),
}


@functools.lru_cache(maxsize=512)
def day(year: int, month: int, day: int) -> datetime:
    """Return a datetime object for the given date"""
    return datetime(year=year, month=month, day=day)


# Pre-compute common week values
_CACHED_WEEKS = {i: timedelta(weeks=i) for i in range(1, 53)}

@functools.lru_cache(maxsize=64)
def weeks(i: int) -> timedelta:
    """ return a timedelta week, with integers as the input """
    if i in _CACHED_WEEKS:
        return _CACHED_WEEKS[i]
    return timedelta(weeks=i)


# Pre-compute common day values
_CACHED_DAYS = {i: timedelta(days=i) for i in range(0, 366)}

@functools.lru_cache(maxsize=366)
def days(numdays: int) -> timedelta:
    """ return a timedelta day(s), with integers as the input """
    if numdays in _CACHED_DAYS:
        return _CACHED_DAYS[numdays]
    return timedelta(days=numdays)


@functools.lru_cache(maxsize=256)
def weekday(date: datetime) -> str:
    """ return the weekday, with datetime as the input """
    return date.strftime('%a')


@functools.lru_cache(maxsize=32)
def leap_year(year: int) -> bool:
    """ return true if year is a leap year """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


@functools.lru_cache(maxsize=128)
def latex_replacement(string: str) -> str:
    """ return a string formatted for LaTeX with escape characters """
    return re.sub('&', r'\&', re.sub('_', r'\_', string))


# Pre-compute the months translation dictionary
_MONTHS_IN_LATIN = {
    'January': 'Januarius',
    'February': 'Februarius',
    'March': 'Martius',
    'April': 'Aprilis',
    'May': 'Majus',
    'June': 'Junis',
    'July': 'Julius',
    'August': 'Augustus',
}

@functools.lru_cache(maxsize=12)
def translate_month(month: str) -> str:
    """ return the latin name for a given english month """
    return _MONTHS_IN_LATIN.get(month, month)


# Pre-compute the sevens list used in which_sunday
_SEVENS = tuple(range(0, 31, 7))

@functools.lru_cache(maxsize=256)
def which_sunday(date: datetime) -> int:
    """
    Determine the numeric order of a Sunday within a month.
    """
    index = int(date.strftime("%d"))
    x = 0
    while index-x not in _SEVENS:
        x += 1
    return _SEVENS.index(index-x)+1


@functools.lru_cache(maxsize=256)
def last_sunday(date: datetime) -> bool:
    """Determine if a date is the last Sunday of the month"""
    sunday_num = which_sunday(date)
    if sunday_num < 4:
        return False
    elif sunday_num == 4 and int(date.strftime("%d")) < 25:
        return False
    else:
        return True
