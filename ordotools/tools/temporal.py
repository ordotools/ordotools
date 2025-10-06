from ordotools.tools.helpers import day
from ordotools.tools.helpers import days
from ordotools.tools.helpers import easter
from ordotools.tools.helpers import findsunday
from ordotools.tools.helpers import last_sunday
from ordotools.tools.helpers import weekday
from ordotools.tools.helpers import weeks
from ordotools.tools.temporal_data import TemporalData


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

    def __init__(self, year):
        self.year = year
        self.easter = easter(self.year)
        self.septuagesima = self.easter - weeks(9)
        self.christmas = day(year=self.year, month=12, day=25)
        self.epiphany = day(self.year, 1, 6)
        self.lastadvent = self.christmas - findsunday(self.christmas)

    def advent(self) -> dict:
        """ Advent Season """
        y = {}
        for x in range(4):
            if x == 0 and self.christmas-days(1) == self.lastadvent:
                y |= {self.lastadvent: "DV_Christmas"}
            else:
                y |= {self.lastadvent-weeks(x): f"D_Advent_{4-x}"}
                for fer in range(2, 8):
                    if x == 1 and fer in [4, 6, 7]:
                        y |= {
                            self.lastadvent-weeks(x)+days(fer-1):
                            f"Ember_Advent_{fer if fer != 7 else 's'}"
                        }
                        pass
                    else:
                        y |= {
                            self.lastadvent-weeks(x)+days(fer-1):
                            f"de_Advent_{4-x}_f{fer if fer != 7 else 's'}"
                        }
        return y

    def christmas_time(self) -> dict:
        """ Christmas and the following days to the end of the year. """
        y = {}
        def d(a): return self.christmas+days(a)
        for x, feast in enumerate([
            "Christmas", "StStephan", "StJohn", "StsInnocents",
            "StThomas", "StSylvester", "8_Chritmas_f6",
        ]):  # TODO: add special keys for 1-3 if they fall on a Sunday
            if d(x).strftime("%a") == "Sun" and x != 0:
                if x in [4, 5]:
                    feast = f"D_{feast}"
                elif x > 5:
                    feast = "D_Christmas"
            y |= {d(x): feast}
        return y

    def start_year(self) -> dict:
        """ Circumcision up to Septuagesima, excluding Epiphany """
        circumcision = day(self.year, 1, 1)
        y = {
            circumcision: "Circumcision",
            circumcision+days(1): "8_Stephen",
            circumcision+days(2): "8_John",
            circumcision+days(3): "8_Innocents",
        }
        if (
                weekday(circumcision) == "Sun"
                or weekday(circumcision) == "Mon"
                or weekday(circumcision) == "Tue"
                ):
            y |= {day(self.year, 1, 2): "SNameJesu_8_Ste"}
        else:
            y |= {circumcision-findsunday(circumcision)+weeks(1): "SNameJesus"}
        return y

    def epiphany_octave(self) -> dict:
        """ Epiphany and its Sundays """
        y = {
            self.epiphany-days(1): "V_Epiphany",
            self.epiphany: "Epiphany",
            self.epiphany+days(7): "8_Epiphany",
        }
        octave_counter = 1
        for x in range(1, 7):
            the_date = self.epiphany+days(x)
            if weekday(the_date) != "Sun":
                if weekday(the_date) == "Sat":
                    y |= {the_date: "8_Epiph_fs"}
                    octave_counter += 1
                else:
                    y |= {
                        the_date: f"8_Epiph_f{octave_counter+1}",
                    }
                    octave_counter += 1
            else:
                y |= {
                    the_date: "D_Epiphany",
                }
                octave_counter += 1
        return y

    def post_epiphany(self) -> list:
        """ All of the Sundays and ferias after Epiphany """
        sunday_after_epiphany = self.epiphany-findsunday(self.epiphany)+weeks(1)

        def date(w, f): return sunday_after_epiphany+weeks(w)+days(f)
        i = 0
        # TODO: add D_HolyFamily as an option
        y = {sunday_after_epiphany: "HolyFamily"}
        while date(i, 0) != self.septuagesima and i+1 < 7:
            if date(i, 0) != sunday_after_epiphany:
                y |= {date(i, 0): f"D_Epiph_{i+1}"}
            else:
                pass
            for j in range(6):
                if date(i, j+1) > self.epiphany+weeks(1):
                    y |= {
                        date(i, j+1):
                        f"de_Epiph_{i+1}_{j+2 if j != 5 else 's'}"
                    }
            i += 1
        return [y, i+1]

    def gesimas(self) -> dict:
        """ Septuagesima to Quinquagesima """
        y = {}
        for i, x in enumerate(["Septuagesima", "Sexagesima", "Quinquagesima"]):
            pre_lent_week = self.easter - weeks(9-i)
            y |= {pre_lent_week: x}
            for feria in range(6):
                if pre_lent_week+days(feria) == self.easter-weeks(6)-days(5):
                    break
                else:
                    y |= {
                        pre_lent_week+days(feria+1):
                        f"de_{x[0:4]}_f{feria+2 if feria != 5 else 's'}"
                    }
        return y

    def lent(self) -> dict:
        """ All of the Sundays and Ferias of Lent, up to Easter """
        for i in range(7):
            if i == 0:
                y = {
                    self.easter-weeks(7-i)+days(3+c):
                    f"""{
                        "de_" if c == 0 else ""
                        }AshWed{f"_f{c+4 if c != 3 else 's'}" if c != 0 else ""}"""
                    for c in range(4)
                }
            else:
                for j in range(7):
                    if i == 1 and j in [3, 5, 6]:
                        y |= {self.easter-weeks(7-i)+days(j): f"Ember_Lent_{j+1 if j != 6 else 's'}"}
                    elif i == 5 and j == 5:
                        y |= {
                            self.easter-weeks(7-i)+days(j):
                            "SevenSorrows"
                        }
                    else:
                        y |= {
                            self.easter-weeks(7-i)+days(j):
                            f"""{"D" if j == 0 else "de"}_{"Lent" if i < 5 else "Passion" if i != 6 else "Palm"}{f"_f{j+1 if j != 6 else 's'}" if j != 0 else f"_{i}"}"""
                        }
        return y

    def post_easter(self) -> dict:
        """ Easter Week """
        d = ["Easter", "8Easter_f", "WhitSaturday"]
        for j, feast in enumerate(d):
            if j == 0:
                y = {self.easter: feast}
            elif j == 1:
                for i in range(2, 7):
                    y |= {self.easter+days(j+i-2): f"{feast}{i}"}
            else:
                y |= {self.easter+days(6): feast}
        return y

    def paschaltime(self) -> dict:
        """
        From Whit Sunday to Pentecost
        There is probably a better way to implement this,
        but this works for now. Not too easy to debug.
        """
        y = {}
        ascension_counter = 1
        solemnity_counter = 1
        for i in range(1, 7):
            if i == 1:
                the_sunday = "WhitSunday"
            elif i == 6:
                the_sunday = "D_Ascension"
                ascension_counter += 1
            else:
                the_sunday = f"D_Easter_{i}"
            d = 1  # easily matches monday with days(1)
            while d != 7:
                if i == 2 and d >= 3:
                    if d == 3:
                        y |= {
                            self.easter+weeks(i)+days(d): "StJoseph",
                            self.easter+weeks(i+1)+days(3): "8_StJoseph",
                        }
                        solemnity_counter += 1
                    else:
                        y |= {self.easter+weeks(i)+days(d): f"{solemnity_counter}_in_8_StJoseph"}
                        solemnity_counter += 1
                elif i == 3 and d <= 3:
                    if d == 3:
                        pass
                    else:
                        y |= {self.easter+weeks(i)+days(d): f"{solemnity_counter}_in_8_StJoseph"}
                        solemnity_counter += 1
                elif i == 5:  # the whole week is special
                    # TODO: clean up the Ascension days
                    if d <= 3:  # rogations
                        y |= {self.easter+weeks(i)+days(d): f"Rogation_{d}"}
                    elif d == 4:
                        y |= {self.easter+weeks(i)+days(d): "Ascension"}
                        ascension_counter += 1
                    elif 4 < d < 6:
                        y |= {self.easter+weeks(i)+days(d): f"""in_8_Ascension_{ascension_counter}"""}
                        ascension_counter += 1
                    elif d == 6:
                        y |= {self.easter+weeks(i)+days(d): f"""{"S_8_" if d != 4 else ""}Ascension"""}
                        ascension_counter += 1
                elif i == 6 and d < 5:
                    y |= {self.easter+weeks(i)+days(d): f"""{"in_8" if d != 4 else "8"}_Ascension{f'_{ascension_counter}' if d != 4 else ""}"""}
                    ascension_counter += 1
                elif i == 6 and d == 6:
                    y |= {self.easter+weeks(i)+days(d): "V_Pentecost"}
                else:
                    y |= {self.easter+weeks(i)+days(d): f"de_Easter_{i}_f{d+1 if d != 6 else 's'}"}
                d += 1
            y |= {self.easter+weeks(i): the_sunday}
            solemnity_counter += 1 if solemnity_counter > 1 else 0
        return y


    def pentecost(self) -> dict:
        """
        All of the days after Pentecost, including the feasts
        and octaves of Corpus Christi and the Sacred Heart.
        """
        pentecost_date = self.easter + weeks(7)
        last_pent = self.christmas - findsunday(self.christmas) - weeks(4)
        y = {pentecost_date: 'Pentecost'}
        for fer in range(2, 8):
            if fer in [4, 6, 7]:
                y |= {
                    pentecost_date+days(fer-1):
                    f"Ember_Pent_{fer if fer != 7 else 's'}"
                }
            else:
                y |= {
                    pentecost_date+days(fer-1):
                    f"8Pent_f{fer if fer != 7 else 's'}"
                }
        x, e = 1, 0
        september_count = 0
        corpuschristi_count = 1
        sacredheart_count = 1
        while pentecost_date+weeks(x) != last_pent+weeks(1):  # i.e., Advent 1
            sunday_date = pentecost_date+weeks(x)
            leftovers = self.post_epiphany()[1]
            chK = ""
            if (
                    last_sunday(pentecost_date+weeks(x)) is True and
                    (pentecost_date+weeks(x)).strftime("%B") == "October"
                    ):
                chK = "ChristKing"
                sunday = f'Pent_{x}'
            elif pentecost_date+weeks(x) == last_pent:
                sunday = f"UltPent_{x}"  # TODO: if the final 23rd, 24th anti.
            elif pentecost_date+weeks(x)+weeks(1) == last_pent-weeks(6-leftovers)+weeks(e):
                sunday = f'Epiph_{leftovers+e}_{x}'
                e += 1
            else:
                sunday = f'Pent_{x}'
            if sunday_date.strftime('%B') == "September":
                september_count += 1
            d = 0
            while d < 7:
                if x == 1 and d == 0:
                    y |= {sunday_date: "Trinity"}
                elif x == 1 and d >= 4:
                    y |= {
                        sunday_date+days(d):
                        f"{f'{corpuschristi_count}_in_8_' if d > 4 else ''}CorpusChristi"
                    }
                    corpuschristi_count += 1
                elif x == 2 and 0 < d <= 4:
                    y |= {
                        sunday_date+days(d):
                        f"{f'{corpuschristi_count+1}_in_8_' if d < 4 else '8_'}CorpusChristi"
                    }
                    corpuschristi_count += 1
                elif x == 2 and d >= 5:
                    y |= {
                        sunday_date+days(d):
                        f"{f'{sacredheart_count}_in_8_' if d > 5 else ''}SacredHeart"
                    }
                    sacredheart_count += 1
                elif x == 3 and 0 < d <= 5:
                    y |= {
                        sunday_date+days(d):
                        f"{f'{sacredheart_count+1}_in_8_' if d < 5 else '8_'}SacredHeart"
                    }
                    sacredheart_count += 1
                elif september_count == 3 and d in [3, 5, 6]:
                    y |= {
                        sunday_date+days(d):
                        f"Ember_Sept_{d+1 if d != 6 else 's'}"
                    }
                elif chK != "" and d == 0:
                    y |= {sunday_date+days(d): "ChristKing"}
                    chK = ""
                else:
                    y |= {
                        sunday_date+days(d):
                        f"""{"de" if d != 0 else "D"}_{sunday}{f"_f{d+1 if d != 6 else 's'}" if d != 0 else ""}"""
                    }
                d += 1
            x += 1
        return y

    def build_entire_year(self) -> dict:
        """
        Returns a dictionary of the entire temporal cycle, but only the
        dates with keys.
        """
        y = {}
        y |= self.advent()
        y |= self.christmas_time()
        y |= self.start_year()
        y |= self.epiphany_octave()
        y |= self.post_epiphany()[0]
        y |= self.gesimas()
        y |= self.lent()
        y |= self.paschaltime()
        y |= self.post_easter()
        y |= self.pentecost()
        return dict(sorted(y.items()))

    def return_temporal(self) -> dict:
        big_data = {}
        data = TemporalData().data
        compiled = self.build_entire_year()
        # TODO: use a loop for this after the data is settled
        for key, value in compiled.items():
            big_data |= {key: {
                "id": data[value]["id"] if value in data.keys() else value,
                "rank": data[value]["rank"],
                # the blue color is easily recognized as incorrect
                "color": data[value]["color"] if value in data.keys() else "blue",
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
                         }
        return big_data
