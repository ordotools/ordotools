from importlib import import_module

import logging

# from ordotools.tools import fasting
from ordotools.tools.commemorations import seasonal_commemorations

from ordotools.tools.feast import Feast

from ordotools.tools.fasting import friday_abstinence
from ordotools.tools.fasting import Fasting

from ordotools.tools.helpers import LiturgicalYearMarks
from ordotools.tools.helpers import days
from ordotools.tools.helpers import ladys_office
from ordotools.tools.helpers import leap_year

from ordotools.tools.rank import rank

from ordotools.tools.translations import Translations
from ordotools.tools.temporal import Temporal

from ordotools.tools.repositories.sanctoral_repo import SanctoralRepository
from ordotools.tools.repositories.translations_repo import TranslationsRepository


class LiturgicalCalendar:

    def __init__(self, year, diocese, language, country=""):
        self.year = year
        self.diocese = diocese
        self.language = language

        # WARN: theoretically we could have more than one transfer
        # self.transfers = None

        self.temporal = Temporal(self.year).return_temporal()

    def expand_octaves(self, feast: Feast) -> tuple:
        octave = ()
        day = 1
        while day < 8:
            # NOTE: since we already have the feast object,
            #       we can just make a function to set the date.
            #       We also have to empty the commemorations.
            new_feast = Feast(
                feast.date+days(day),
                {
                    "id": feast.id+1,
                    "rank": [feast.rank_n, feast.rank_v],
                    "infra_octave_name": feast.infra_octave_name,
                    "day_in_octave": feast.day_in_octave,
                    "color": feast.color,
                    "mass": feast.mass,
                    # FIX: this is probably cusing blank commemorations.
                    "com_1": feast.com_1 if feast.com_1 is not None else {},
                    "com_2": feast.com_2 if feast.com_2 is not None else {},
                    "com_3": feast.com_3 if feast.com_3 is not None else {},
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": feast.vespers,
                    "compline": {},
                    "nobility": feast.nobility,
                    "office_type": feast.office_type,
                }
            )
            if day == 8:
                new_feast.day_in_octave = day
            else:
                new_feast.day_in_octave = day
            new_feast.fasting = False
            # WARN: Verify that this is always the case:
            new_feast.rank_v = "sd"
            new_feast.rank_n = 18 if day < 6 else 13
            new_feast.reset_commemorations()
            octave += (new_feast,)
            day += 1
        return octave

    def find_octave(self, year: tuple) -> tuple:
        year = list(year)
        temporals = [feast["id"] for feast in self.temporal.values()]
        for candidate in year:
            if isinstance(candidate, list):
                print(f"list of {candidate[0].id} and {candidate[1].id}")
            if candidate.id in temporals:
                continue
            elif candidate.octave is True:
                logging.debug(f"Building octave for {candidate.id} with octave set to {candidate.octave}")
                position = year.index(candidate)
                octave = self.expand_octaves(candidate)
                octave_days = self.add_feasts(master=year[position:position+8], addition=octave)
        year[position:position+8] = octave_days
        return year

    def build_feasts(self, candidates: dict) -> tuple:
        feasts = ()
        for date, data in candidates.items():
            feast = Feast(date, data, lang=self.language)
            feasts += (feast,)
        return feasts

    def initialize(self, to_initialize: list):
        inititalized = {
            "temporal": (),
            "sanctoral": (),
        }
        for i, dictionary in enumerate(to_initialize):
            if i == 0:
                inititalized["temporal"] += self.build_feasts(dictionary)
            else:
                inititalized["sanctoral"] += self.build_feasts(dictionary)
        return inititalized

    def add_feasts(self, master: tuple, addition: tuple) -> tuple:
        calendar = []
        master_expanded = {}
        for feast in master:
            master_expanded.update({feast.date: feast})
        addition_expanded = {}
        for feast in addition:
            addition_expanded.update({feast.date: feast})
        for date in master_expanded.keys():
            if date in addition_expanded.keys():
                feast = rank(
                    dynamic=addition_expanded[date],
                    static=master_expanded[date]
                )
            else:
                feast = master_expanded[date]
            if isinstance(feast, list):
                # anticipations
                anticipated = feast[1]
                new_last_feast = rank(
                    dynamic=anticipated,
                    static=calendar[-1]
                )
                calendar[-1] = new_last_feast
                calendar.append(feast[0])
            else:
                calendar.append(feast)
        return tuple(calendar)

    def our_ladys_saturday(self, calendar: tuple) -> tuple:
        """
        Adds Office of the Blessed Virgin Mary on Saturdays.

        In omnibus Sabbatis per annum extra Adventum et Quadragesimam, ac nisi
        Quatuor tempora aut Vigilia; occurrant, vel nisi fieri debeat de Feria
        propter Officium alicujus Dominica; aliquando infra Hebdomadam ponendum
        , ut in Rubrica de Dominicis dictum est; et nisi fiat Officium novem
        Lectionum, vel de Octava Pascha; et Pentecostes, semper fit Officium de
        sancta Maria, eo modo, quo fit de Festo Simplici, quemadmodum circa
        finem Breviarii disponitur. De Festo autem Simplici, in Sabbato
        occurrente, fit tantum commemoratio.
        """
        year = list(calendar)
        office = ladys_office  # TODO: add this according to the season
        for pos, feast in enumerate(year):
            if feast.date.strftime("%w") == str(6):
                first_advent = LiturgicalYearMarks(self.year).first_advent
                last_advent = LiturgicalYearMarks(self.year).last_advent
                lent_begins = LiturgicalYearMarks(self.year).lent_begins
                lent_ends = LiturgicalYearMarks(self.year).lent_ends
                if lent_begins <= feast.date <= lent_ends:
                    continue
                elif first_advent <= feast.date <= last_advent:
                    continue
                else:
                    if feast.rank_n > 20:
                        # FIX: there should be a commemoration here for the replaced feast?
                        year[pos] = Feast(feast.date, office, lang=self.language)
                    else:
                        continue
        return tuple(year)

    def add_translation(self, compiled_calendar: tuple) -> list:
        """
        Finds the translation for each feast id
        """
        year = []
        translations = Translations()
        for feast in compiled_calendar:
            if isinstance(feast.id, int):
                if feast.id % 10 == 1:
                    feast.name = translations.octave(self.language, feast.day_in_octave, feast.id)
                else:
                    feast.name = translations.translations()[feast.id][self.language]
            else:
                feast.name = translations.translations()[feast.id][self.language]

            # NOTE: just for the commemorations
            if "id" in feast.com_1.keys() and feast.com_1["id"] is not None:
                feast.com_1["name"] = translations.translations()[feast.com_1["id"]][self.language]
            else:
                feast.com_1["name"] = None
            if "id" in feast.com_2.keys() and feast.com_2["id"] is not None:
                feast.com_2["name"] = translations.translations()[feast.com_2["id"]][self.language]
            else:
                feast.com_2["name"] = None
            if "id" in feast.com_3.keys() and feast.com_3["id"] is not None:
                feast.com_3["name"] = translations.translations()[feast.com_3["id"]][self.language]
            else:
                feast.com_3["name"] = None

            year.append(feast)
        return year

    def build(self) -> list:
        # Load sanctoral data from database
        repo = SanctoralRepository()
        sanctoral = repo.get_year_calendar(self.diocese)
        # Update date keys to use actual year instead of dummy year
        from datetime import datetime
        sanctoral_updated = {}
        for date_key, feast_data in sanctoral.items():
            new_date = datetime(year=self.year, month=date_key.month, day=date_key.day)
            sanctoral_updated[new_date] = feast_data
        sanctoral = sanctoral_updated
        repo.close()
        
        logging.info('Initializing...')
        initialized = self.initialize([self.temporal, sanctoral])
        logging.info('Adding the calendars together...')
        full_calendar = self.add_feasts(initialized["temporal"], initialized["sanctoral"])
        logging.info('Building octaves...')
        full_calendar = self.find_octave(year=full_calendar)
        logging.info("Adding Our Lady's Saturday...")
        full_calendar = self.our_ladys_saturday(full_calendar)
        logging.info('Building seasonal commemorations...')
        full_calendar = seasonal_commemorations(feasts=full_calendar, year=self.year)
        logging.info('Translating...')
        full_calendar = self.add_translation(full_calendar)

        # set the fasting rules
        # OPTIM: add this in on initiation, perhaps
        logging.info('Adding Friday abstinence...')
        for feast in full_calendar:
            friday_abstinence(feast)  # this might be better in Feast

        logging.info('Adding the Lenten fast...')
        fasting_rules = Fasting(self.year)
        for feast in full_calendar:
            fasting_rules.fasting_day_lent(feast)

        logging.info('Complete!')
        return list(full_calendar)
