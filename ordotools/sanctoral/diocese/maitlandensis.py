from ordotools.tools.helpers import day
from importlib import import_module


class Diocese:
    """
    Proper days of a diocese, which calls a country.
    """

    def __init__(self, year):
        self.year = year

        self.name = "D. Maitlanden"
        self.country = "australiae"

        self.sanctoral = import_module(f"ordotools.sanctoral.country.{self.country}")
        self.country_data = self.sanctoral.Country(self.year).data
        self.roman = import_module("ordotools.sanctoral.diocese.roman")
        self.roman_data = self.roman.Sanctoral(self.year).data

        self.data = {
            day(year=self.year, month=3, day=17): {
                # This feast has a Common Octave if it is transferred outside
                # of Lent, which happens if Easter is between March 22 and
                # March 24.
                "feast": "S. Patritii E.C. Patroni Hiberniae",
                "rank": [5, "d I cl"],  # check the ranking
                "nobility": (False,),
                "com": [],
                "office_type": False,
                "color": "white",
                "mass": {
                    "int": "Statuit",
                    "glo": True,
                    "cre": True,
                    "pre": "Communis"
                },
                "matins": {
                    "L1": "",
                    "L2": "",
                    "L3": "",
                    "L4": "",
                    "L5": "",
                    "L6": "",
                    "L7": "",
                    "L8": "",
                    "L9": "",
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                # common antiphons
                "vespers": {
                    "proper": False,
                    "admag": ("Sacerdos et Pontifex", "Amavit eum Dominus"),
                    "propers": {
                        "hymn": "",
                        "verse": ""
                    },
                    "oration": "Deus, qui ad praedicandam"
                },
                "compline": {},
                "fasting": False,
            }
        }

    def calendar(self) -> dict:
        y = {}
        for local in self.data:
            # HACK: just to get things started
            if local in self.country_data:
                y |= {local: self.data[local]}
            else:
                y |= {local: self.data[local]}
        for date in self.roman_data:
            if date in y:
                # HACK: just to get things started
                pass
            else:
                y |= {date: self.roman_data[date]}
        return y
