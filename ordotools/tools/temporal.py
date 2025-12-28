from functools import cached_property
import functools

from ordotools.tools.helpers import day
from ordotools.tools.helpers import days
from ordotools.tools.helpers import easter
from ordotools.tools.helpers import findsunday
from ordotools.tools.helpers import last_sunday
from ordotools.tools.helpers import weekday
from ordotools.tools.helpers import weeks
from ordotools.tools.repositories.temporal_repo import TemporalRepository


class Temporal:
    """
    This class will enable us to explore parts of the liturgical year, rather
    than having to calulate the entire year. The exact implementation process
    is still being worked out, but this class will be much easier to debug and
    develop rather than the previous idea.

    For the various parts of the year that require more advanced
    configurations, (e.g. the O-antiphons) this modular approach will allow the
    parts of the year to be self-calculated, which will be more efficient in
    the long run, and allow for much easier debugging. Having already tried the
    "figure it out in one go" approach, I can tell you that this is the way to
    go.

    Some of the f-strings and dictionary comprehensions might be too cumbersome
    for some tastes, but in this case they save quite a bit of time and
    debugging.

    The lack of verboseness in some of the naming conventions is intentional
    (e.g., not mentioning "Holy Saturday" explicitly, but naming it the
    Saturday feria in "Palm Sunday" week). The job is accomplished sufficiently
    with the current naming system, and to try to give the most appropriate
    name to everything would result in a file that is overly long and
    complicated.
    """
    # Class-level cache to avoid recreating Temporal instances
    _instances = {}

    def __new__(cls, year):
        # Return cached instance if available
        if year in cls._instances:
            return cls._instances[year]
            
        # Create new instance
        instance = super(Temporal, cls).__new__(cls)
        cls._instances[year] = instance
        return instance

    def __init__(self, year):
        # Skip initialization if already initialized
        if hasattr(self, 'year') and self.year == year:
            return
            
        self.year = year
        self._easter_date = easter(self.year)
        self._christmas_date = day(year=self.year, month=12, day=25)
        self._epiphany_date = day(self.year, 1, 6)
        
        # Pre-calculate commonly used date values
        self.easter = self._easter_date
        self.septuagesima = self._easter_date - weeks(9)
        self.christmas = self._christmas_date
        self.epiphany = self._epiphany_date
        self.lastadvent = self._christmas_date - findsunday(self._christmas_date)

    @cached_property
    def advent(self) -> dict:
        """ Advent Season """
        y = {}
        for x in range(4):
            if x == 0 and self.christmas-days(1) == self.lastadvent:
                y |= {self.lastadvent: "DV_Christmas"}
            else:
                advent_sunday = self.lastadvent-weeks(x)
                y |= {advent_sunday: f"D_Advent_{4-x}"}
                for fer in range(2, 8):
                    feria_date = advent_sunday+days(fer-1)
                    if x == 1 and fer in [4, 6, 7]:
                        y |= {
                            feria_date:
                            f"Ember_Advent_{fer if fer != 7 else 's'}"
                        }
                    else:
                        y |= {
                            feria_date:
                            f"de_Advent_{4-x}_f{fer if fer != 7 else 's'}"
                        }
        return y

    @cached_property
    def christmas_time(self) -> dict:
        """ Christmas and the following days to the end of the year. """
        y = {}
        
        # Pre-calculate dates and store in a list to avoid repeated calculations
        christmas_days = [self.christmas+days(a) for a in range(7)]
        
        feasts = [
            "Christmas", "StStephan", "StJohn", "StsInnocents",
            "StThomas", "StSylvester", "8_Chritmas_f6",
        ]
        
        for x, feast in enumerate(feasts):  # TODO: add special keys for 1-3 if they fall on a Sunday
            date = christmas_days[x]
            if weekday(date) == "Sun" and x != 0:
                if x in [4, 5]:
                    feast = f"D_{feast}"
                elif x > 5:
                    feast = "D_Christmas"
            y |= {date: feast}
        return y

    @cached_property
    def start_year(self) -> dict:
        """ Circumcision up to Septuagesima, excluding Epiphany """
        circumcision = day(self.year, 1, 1)
        
        # Pre-calculate common dates
        january_days = [circumcision+days(i) for i in range(4)]
        
        y = {
            january_days[0]: "Circumcision",
            january_days[1]: "8_Stephen",
            january_days[2]: "8_John",
            january_days[3]: "8_Innocents",
        }
        
        circumcision_weekday = weekday(circumcision)
        if (circumcision_weekday == "Sun" or
            circumcision_weekday == "Mon" or
            circumcision_weekday == "Tue"):
            y |= {day(self.year, 1, 2): "SNameJesu_8_Ste"}
        else:
            y |= {circumcision-findsunday(circumcision)+weeks(1): "SNameJesus"}
        return y

    @cached_property
    def epiphany_octave(self) -> dict:
        """ Epiphany and its Sundays """
        y = {
            self.epiphany-days(1): "V_Epiphany",
            self.epiphany: "Epiphany",
            self.epiphany+days(7): "8_Epiphany",
        }
        
        # Pre-calculate epiphany dates
        epiphany_dates = [self.epiphany+days(x) for x in range(1, 7)]
        
        octave_counter = 1
        for x in range(6):
            the_date = epiphany_dates[x]
            date_weekday = weekday(the_date)
            
            if date_weekday != "Sun":
                if date_weekday == "Sat":
                    y |= {the_date: "8_Epiph_fs"}
                else:
                    y |= {the_date: f"8_Epiph_f{octave_counter+1}"}
            else:
                y |= {the_date: "D_Epiphany"}
                
            octave_counter += 1
            
        return y

    @cached_property
    def post_epiphany(self) -> list:
        """ All of the Sundays and ferias after Epiphany """
        sunday_after_epiphany = self.epiphany-findsunday(self.epiphany)+weeks(1)
        epiphany_plus_one_week = self.epiphany+weeks(1)
        
        # Function to calculate date with memoization
        @functools.lru_cache(maxsize=128)
        def calc_date(w, f):
            return sunday_after_epiphany+weeks(w)+days(f)
            
        i = 0
        # TODO: add D_HolyFamily as an option
        y = {sunday_after_epiphany: "HolyFamily"}
        
        while calc_date(i, 0) != self.septuagesima and i+1 < 7:
            sunday_date = calc_date(i, 0)
            if sunday_date != sunday_after_epiphany:
                y |= {sunday_date: f"D_Epiph_{i+1}"}
                
            for j in range(6):
                feria_date = calc_date(i, j+1)
                if feria_date > epiphany_plus_one_week:
                    y |= {
                        feria_date:
                        f"de_Epiph_{i+1}_{j+2 if j != 5 else 's'}"
                    }
            i += 1

        return [y, i+1]

    # TODO: Christ the King is on the last Sunday of October

    @cached_property
    def gesimas(self) -> dict:
        """ Septuagesima to Quinquagesima """
        y = {}
        gesima_names = ["Septuagesima", "Sexagesima", "Quinquagesima"]
        ash_wednesday = self.easter-weeks(6)-days(4)
        
        for i, gesima_name in enumerate(gesima_names):
            pre_lent_week = self.easter - weeks(9-i)
            y |= {pre_lent_week: gesima_name}
            
            # Pre-calculate prefix and weekday dates
            prefix = gesima_name[0:4]
            weekday_dates = [pre_lent_week+days(feria+1) for feria in range(6)]
            
            for feria, date in enumerate(weekday_dates):
                if date >= ash_wednesday:
                    break
                else:
                    y |= {
                        date:
                        f"de_{prefix}_f{feria+2 if feria != 5 else 's'}"
                    }
        return y

    @cached_property
    def lent(self) -> dict:
        """ All of the Sundays and Ferias of Lent, up to Easter """
        y = {}
        
        # Pre-calculate common date calculations
        ash_wednesday = self.easter - weeks(6) - days(4)
        
        # First week (Ash Wednesday and days after)
        ash_week_dates = [ash_wednesday + days(c) for c in range(4)]
        for c, date in enumerate(ash_week_dates):
            if c == 0:
                y[date] = "de_AshWed"
            else:
                y[date] = f"AshWed_f{c+4 if c != 3 else 's'}"
        
        # Remaining weeks of Lent
        for i in range(1, 7):
            lent_sunday = self.easter - weeks(7-i)
            
            # Pre-calculate all dates for this week
            week_dates = [lent_sunday + days(j) for j in range(7)]
            
            for j, date in enumerate(week_dates):
                if i == 1 and j in [3, 5, 6]:
                    y[date] = f"Ember_Lent_{j+1 if j != 6 else 's'}"
                elif i == 5 and j == 5:
                    y[date] = "SevenSorrows"
                else:
                    # Determine season name
                    if i < 5:
                        season = "Lent"
                    elif i == 5:
                        season = "Passion"
                    else:
                        season = "Palm"
                    
                    # Create entry name
                    prefix = "D" if j == 0 else "de"
                    suffix = f"_{i}" if j == 0 else f"_f{j+1 if j != 6 else 's'}"
                    
                    y[date] = f"{prefix}_{season}{suffix}"
        
        return y

    @cached_property
    def post_easter(self) -> dict:
        """ Easter Week """
        y = {self.easter: "Easter"}
        
        # Pre-calculate Easter week dates
        easter_weekdays = [self.easter + days(i) for i in range(1, 7)]
        
        # Monday through Friday
        for i, date in enumerate(easter_weekdays[:-1]):
            y[date] = f"8Easter_f{i+2}"
            
        # Saturday
        y[easter_weekdays[-1]] = "WhitSaturday"
        
        return y

    @cached_property
    def paschaltime(self) -> dict:
        """
        From Whit Sunday to Pentecost
        There is probably a better way to implement this,
        but this works for now. Not too easy to debug.
        """
        y = {}
        ascension_counter = 1
        solemnity_counter = 1
        
        # Pre-calculate common dates
        easter_weeks = [self.easter + weeks(i) for i in range(1, 7)]
        
        for i in range(1, 7):
            week_index = i - 1  # For accessing pre-calculated weeks
            
            # Determine Sunday name
            if i == 1:
                the_sunday = "WhitSunday"
            elif i == 6:
                the_sunday = "D_Ascension"
                ascension_counter += 1
            else:
                the_sunday = f"D_Easter_{i}"
# <<<<<<< HEAD
#             d = 1  # easily matches monday with days(1)
#             while d != 7:
# =======
                
            # Add Sunday
            sunday_date = easter_weeks[week_index]
            y[sunday_date] = the_sunday
            
            # Pre-calculate weekday dates for this week
            weekday_dates = [sunday_date + days(d) for d in range(1, 7)]
            
            # Process each weekday
            for d, date in enumerate(weekday_dates, 1):  # d starts at 1
# >>>>>>> 0cd0f57ecb7dec0ea24f7fea9e9cb3ff4e8ab386
                if i == 2 and d >= 3:
                    if d == 3:
                        y[date] = "StJoseph"
                        y[easter_weeks[i] + days(3)] = "8_StJoseph"
                        solemnity_counter += 1
                    else:
                        y[date] = f"{solemnity_counter}_in_8_StJoseph"
                        solemnity_counter += 1
                elif i == 3 and d <= 3:
                    if d == 3:
                        pass  # Skip this date
                    else:
                        y[date] = f"{solemnity_counter}_in_8_StJoseph"
                        solemnity_counter += 1
                elif i == 5:  # the whole week is special
                    # TODO: clean up the Ascension days
                    if d <= 3:  # rogations
# <<<<<<< HEAD
#                         y |= {self.easter+weeks(i)+days(d): f"Rogation_{d}"}
# =======
                        y[date] = f"Rogation_{d}"
# >>>>>>> 0cd0f57ecb7dec0ea24f7fea9e9cb3ff4e8ab386
                    elif d == 4:
                        y[date] = "Ascension"
                        ascension_counter += 1
                    elif 4 < d < 6:
                        y[date] = f"in_8_Ascension_{ascension_counter}"
                        ascension_counter += 1
                    elif d == 6:
                        y[date] = f"S_8_Ascension"
                        ascension_counter += 1
                elif i == 6 and d < 5:
                    if d == 4:
                        y[date] = "8_Ascension"
                    else:
                        y[date] = f"in_8_Ascension_{ascension_counter}"
                    ascension_counter += 1
                elif i == 6 and d == 6:
                    y[date] = "V_Pentecost"
                else:
                    y[date] = f"de_Easter_{i}_f{d+1 if d != 6 else 's'}"
            
            solemnity_counter += 1 if solemnity_counter > 1 else 0
            
        return y


    @cached_property
    def pentecost(self) -> dict:
        """
        All of the days after Pentecost, including the feasts
        and octaves of Corpus Christi and the Sacred Heart.
        """
        pentecost_date = self.easter + weeks(7)
        last_pent = self.christmas - findsunday(self.christmas) - weeks(4)
        y = {pentecost_date: 'Pentecost'}
        
        # Pre-calculate pentecost week dates
        pentecost_weekdays = [pentecost_date + days(fer-1) for fer in range(2, 8)]
        
        # Process pentecost week
        for i, (fer, date) in enumerate(zip(range(2, 8), pentecost_weekdays)):
            if fer in [4, 6, 7]:
                y[date] = f"Ember_Pent_{fer if fer != 7 else 's'}"
            else:
                y[date] = f"8Pent_f{fer if fer != 7 else 's'}"
        
        # Process remaining Sundays after Pentecost
        x, e = 1, 0
        september_count = 0
        corpuschristi_count = 1
        sacredheart_count = 1
        
        # Get leftovers from post-epiphany once to avoid repeated calculations
        leftovers = self.post_epiphany[1]
        
        while pentecost_date + weeks(x) != last_pent + weeks(1):  # i.e., until Advent 1
            sunday_date = pentecost_date + weeks(x)
            chK = ""
            
            # Determine Sunday name
            is_last_sunday_october = (last_sunday(sunday_date) is True and 
                                      sunday_date.strftime("%B") == "October")
            
            if is_last_sunday_october:
                chK = "ChristKing"
                sunday = f'Pent_{x}'
            elif sunday_date == last_pent:
                sunday = f"UltPent_{x}"  # TODO: if the final 23rd, 24th anti.
            elif sunday_date + weeks(1) == last_pent - weeks(6-leftovers) + weeks(e):
                sunday = f'Epiph_{leftovers+e}_{x}'
                e += 1
            else:
                sunday = f'Pent_{x}'
                
            # Track September for Ember days
            if sunday_date.strftime('%B') == "September":
                september_count += 1
                
            # Pre-calculate weekday dates
            week_dates = [sunday_date + days(d) for d in range(7)]
            
            # Process each day of the week
            for d, date in enumerate(week_dates):
                if x == 1 and d == 0:
                    y[date] = "Trinity"
                elif x == 1 and d >= 4:
                    if d > 4:
                        y[date] = f"{corpuschristi_count}_in_8_CorpusChristi"
                    else:
                        y[date] = "CorpusChristi"
                    corpuschristi_count += 1
                elif x == 2 and 0 < d <= 4:
                    if d < 4:
                        y[date] = f"{corpuschristi_count+1}_in_8_CorpusChristi"
                    else:
                        y[date] = "8_CorpusChristi"
                    corpuschristi_count += 1
                elif x == 2 and d >= 5:
                    if d > 5:
                        y[date] = f"{sacredheart_count}_in_8_SacredHeart"
                    else:
                        y[date] = "SacredHeart"
                    sacredheart_count += 1
                elif x == 3 and 0 < d <= 5:
                    if d < 5:
                        y[date] = f"{sacredheart_count+1}_in_8_SacredHeart"
                    else:
                        y[date] = "8_SacredHeart"
                    sacredheart_count += 1
                elif september_count == 3 and d in [3, 5, 6]:
                    y[date] = f"Ember_Sept_{d+1 if d != 6 else 's'}"
                elif chK != "" and d == 0:
                    y[date] = "ChristKing"
                    chK = ""
                else:
                    prefix = "de" if d != 0 else "D"
                    suffix = f"_f{d+1 if d != 6 else 's'}" if d != 0 else ""
                    y[date] = f"{prefix}_{sunday}{suffix}"
                    
            x += 1
            
        return y

    @cached_property
    def build_entire_year(self) -> dict:
        """
        Returns a dictionary of the entire temporal cycle, but only the
        dates with keys.
        """
        y = {}
        y.update(self.advent)
        y.update(self.christmas_time)
        y.update(self.start_year)
        y.update(self.epiphany_octave)
        y.update(self.post_epiphany[0])
        y.update(self.gesimas)
        y.update(self.lent)
        y.update(self.paschaltime)
        y.update(self.post_easter)
        y.update(self.pentecost)
        return dict(sorted(y.items()))

    @cached_property
    def _temporal_data(self):
        """Cache the temporal data to avoid creating it multiple times"""
        repo = TemporalRepository()
        data = repo.get_all_feasts()
        repo.close()
        return data
        
    def return_temporal(self) -> dict:
        big_data = {}
        data = self._temporal_data
        compiled = self.build_entire_year
        
        # Pre-calculate data keys for faster lookups
        data_keys = set(data.keys())
        
        # TODO: use a loop for this after the data is settled
        for key, value in compiled.items():
            value_in_data = value in data_keys
            
            # Prepare field values outside the dictionary creation
            id_value = data[value]["id"] if value_in_data else value
            color_value = data[value]["color"] if value_in_data else "blue"
            
            # Use update instead of |= for better performance
            big_data[key] = {
                "id": id_value,
                "rank": data[value]["rank"],
                "color": color_value,
                "mass": data[value]["mass"],
                "com_1": data[value]["com_1"],
                "com_2": data[value]["com_2"],
                "com_3": data[value]["com_3"],
                "matins": data[value]["matins"],
                "lauds": data[value]["lauds"],
                "prime": data[value]["prime"],
                "little_hours": data[value]["little_hours"],
                "vespers": data[value]["vespers"],
                "compline": data[value]["compline"],
                "office_type": data[value]["office_type"],
                "nobility": data[value]["nobility"],
            }
        return big_data
