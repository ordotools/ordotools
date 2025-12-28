from ordotools.tools.helpers import day


class Sanctoral:
    """
    The Roman Sanctoral Cycle, which is called at every compilation.
    | self.sanctoral is the only return, containing a dictionary of
    | the feasts.
    """

    def __init__(self, year):
        self.year = year
        self.data = {

            # what is the best way to determine if the third lessons are proper?

            # TODO: We need to have a method for events on any day. Greater Litanies, for example.

            # January
            day(year=self.year, month=1, day=5): {
                # S Telesphori PM
                "id": 100000,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                # TODO: get the correct antiphons
                "vespers": {"proper": False, "admag": ("O Doctor", "O Doctor"), "oration": "Deus, qui populo"},
                "compline": {},
            },

            day(year=self.year, month=1, day=14): {
                # S Hilarii Episcopi ECD
                "id": 100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "id": 27400,
                    "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"},
                    "matins": {
                        "lessons": 9,
                    },
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("O Doctor", "O Doctor"), "oration": "Deus, qui populo"},
                "compline": {},
            },

            day(year=self.year, month=1, day=15): {
                # S Pauli Primi Eremitæ C
                "id": 200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 27500,
                    "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=16): {
                # S Marcelli PM
                "id": 300,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=17): {
                # S Antonii Abb
                "id": 400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=18): {
                # Cathedræ S Petri Ap Romæ
                "id": 500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    "id": 27600,
                    "mass": False
                },
                "com_2": {
                    "id": 27700,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": True, "pre": "Communis"}
                },
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=19): {
                # Ss Marii, Marthæ, Audifacis et Abachum Mm
                "id": 600,
                "rank": [22, "s"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Justi epulentur", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 27800,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=20): {
                # Ss Fabiani P et Sebastiani Mm
                "id": 700,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret in conspectu", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=21): {
                # S Agnetis VM
                "id": 800,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=22): {
                # Ss Vincentii & Anastasii Mm
                "id": 900,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=23): {
                # S Raymundi de Peñafort C
                "id": 1000,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 27900,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=24): {
                # S Timothei EM
                "id": 1100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=25): {
                # Conversio S Pauli Ap
                "id": 1200,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Scio, cui credidi", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    "id": 28000,
                    "mass": False
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=26): {
                # S Polycarpi EM
                "id": 1300,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=27): {
                # S Joannis Chrysostomi ECD
                "id": 1400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=28): {
                # S Petri Nolasci C
                "id": 1500,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 28100,
                    "mass": {"int": "Vultum tuum", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=29): {
                # S Francisci Salesii ECD
                "id": 1600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=30): {
                # S Martinæ VM
                "id": 1700,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=31): {
                # S Joannis Bosco C
                "id": 1800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dedit illi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # February
            day(year=self.year, month=2, day=1): {
                # S Ignatii EM
                "id": 1900,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=2): {
                # In Purificatione BMV
                "id": 2000,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Suscepisimus", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=3): {
                # S Blasii EM
                "id": 2100,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=4): {
                # S Andreæ Corsini EC
                "id": 2200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=5): {
                # S Agathæ VM
                "id": 2300,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=6): {
                # S Titi EC
                "id": 2400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 28200,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=7): {
                # S Romualdi Abb
                "id": 2500,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=8): {
                # S Joannis de Matha C
                "id": 2600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=9): {
                # S Cyrilli Alexandrini ECD
                "id": 2700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "id": 28300,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=10): {
                # S Scholasticæ V
                "id": 2800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=11): {
                # In Apparitione BMV Immaculatæ
                "id": 2900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Vidi civitatem", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=12): {
                # Ss Septem Fundatores Ordinis Servorum BMV C
                "id": 3000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justi decantaverunt", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=14): {
                # S Valentini PM
                "id": 3100,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=15): {
                # Ss Faustini & Jovitæ Mm
                "id": 3200,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=18): {
                # S Simeonis EM
                "id": 3300,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=22): {
                # In Cathedra S Petri Ap
                "id": 3400,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei Dominus", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=23): {
                # S Petri Damiani ECD
                "id": 3500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "id": 27300,
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=24): {
                # S Matthiæ Ap
                "id": 3600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=27): {
                # S Gabrielis a Virgine Perdolente C
                "id": 3700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Oculus Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # March
            day(year=self.year, month=3, day=4): {
                # S Casimiri C
                "id": 3800,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 28400,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=6): {
                # Ss Perpetuae et Felicitatiis Mm
                "id": 3900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=7): {
                # S Thomæ de Aquino CD
                "id": 4000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=8): {
                # S Joannis a Deo C
                "id": 4100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=9): {
                # S Franciscae Romanae V
                "id": 4200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=10): {
                # Ss Quadragintarum Mm
                "id": 4300,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Clamaverunt iusti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=12): {
                # S Gregorii I PCD
                "id": 4400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=17): {
                # S Patricii EC
                "id": 4500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=18): {
                # S Cyrilli Hierosolymitani ECD
                "id": 4600,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=19): {
                # S Josephi Sponsi BMV C
                "id": 4700,
                "rank": [2, "d I cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": True, "pre": "De Sancto Ioseph"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=21): {
                # S Benedicti Abb
                "id": 4800,
                "rank": [14, "dm"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=24): {
                # S Gabrielis Arch
                "id": 4900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite Dominum", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=25): {
                # In Annuntiatione BMV
                "id": 5000,
                "rank": [2, "d I cl"],
                "nobility": (1, 2, 6, 2, 1, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Vultum tuum", "glo": True, "cre": True, "pre": "De B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=27): {
                # S Joannis Damasceni CD
                "id": 5100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Tenuisti manum", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=3, day=28): {
                # S Joannis a Capistrano C
                "id": 5200,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ego autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # April
            day(year=self.year, month=4, day=2): {
                # S Francisci de Paula C
                "id": 5300,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=4): {
                # S Isidori ECD
                "id": 5400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=5): {
                # S Vincentii Ferrerii C
                "id": 5500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=11): {
                # S Leonis PCD
                "id": 5600,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=13): {
                # S Hermenegildi M
                "id": 5700,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=14): {
                # S Justini M
                "id": 5800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Narraverunt mihi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 28500,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=17): {
                # S Aniceti PM
                "id": 5900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=21): {
                # S Anselmi ECD
                "id": 6000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=22): {
                # Ss Soteris et Caii PpMm
                "id": 6100,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=23): {
                # S Georgii M
                "id": 6200,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=24): {
                # S Fidelis a Sigmaringa M
                "id": 6300,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=25): {
                # S Marci Ev
                "id": 6400,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=26): {
                # Ss Cleti et Marcellini PpMm
                "id": 6500,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=27): {
                # S Petri Canisii CD
                "id": 6600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=28): {
                # S Pauli a Cruce C
                "id": 6700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Christo confixus sum", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 28600,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=29): {
                # S Petri M
                "id": 6800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=30): {
                # S Catharinae Senensis V
                "id": 6900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # May
            day(year=self.year, month=5, day=1): {
                # Ss Philippi et Iacobi App
                "id": 7000,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Clamaverunt ad te", "glo": True, "cre": True, "pre": "De Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=2): {
                # S Athanasii ECD
                "id": 7100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=3): {
                # In Inventione S Crucis
                "id": 7200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Nos autem gloriari", "glo": True, "cre": True, "pre": "De Cruce"},
                "com_1": {
                    "id": 28700,
                    "mass": {"int": "Sancti tui", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=4): {
                # S Monicae V
                "id": 7300,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi, Domine", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=5): {
                # S Pii V PC
                "id": 7400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=6): {
                # S Joannis ApEv ante Portam Latinam
                "id": 7500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Protexisti me", "glo": True, "cre": True, "pre": "De Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=7): {
                # S Stanislai EM
                "id": 7600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=8): {
                # In Apparitione S Michaelis Arch
                "id": 7700,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite Dominum", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=9): {
                # S Gregorii Nanzanzeni ECD
                "id": 7800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In media", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=10): {
                # S Antonini EC
                "id": 7900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 28800,
                    "mass": {"int": "Sancti tui", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=12): {
                # Ss Nerei, Achillei at Domitillae V atq Pancratii Mm
                "id": 8000,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Ecce, oculi Domini", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=13): {
                # S Roberti Bellarmino ECD
                "id": 8100,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=14): {
                # S Bonifatii M
                "id": 8200,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=15): {
                # S Joannis Baptistae de la Salle C
                "id": 8300,
                "rank": [15, "d, mtv"],  # TODO: check this mtv
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=16): {
                # S Ubaldi EC
                "id": 8400,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=17): {
                # S Paschalis Baylon C
                "id": 8500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=18): {
                # S Venantii M
                "id": 8600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=19): {
                # S Petri Caelestini PC
                "id": 8700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    "id": 28900,
                    "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=20): {
                # S Bernardini Senensis C
                "id": 8800,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=25): {
                # S Gregorii VII PC
                "id": 8900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    "id": 29000,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=26): {
                # S Philippi Nerii C
                "id": 9000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Caritas Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "id": 29100,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=27): {
                # S Bedæ Venerabilis CD
                "id": 9100,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "id": 29200,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=28): {
                # S Augustini EC
                "id": 9200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sacerdotes", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=29): {
                # S Mariæ Magdalenæ de Pazzis V
                "id": 9300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=30): {
                # S Felix I PM
                "id": 9400,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=31): {
                # B Mariae Virginis Reginae
                "id": 9500,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Petronillae V
                    "id": 29300,
                    "mass": {"int": "Vultum tuum", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # June
            day(year=self.year, month=6, day=1): {
                # S Angelæ Mericiæ V
                "id": 9600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=2): {
                # Ss Marcellini, Petri atq Erasmi E Mm
                "id": 9700,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=4): {
                # S Francisci Caracciolo C
                "id": 9800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Factum est", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=5): {
                # S Bonifatii EM
                "id": 9900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Exsultabo", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=6): {
                # S Norberti EC
                "id": 10000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=9): {
                # Ss Primi et Feliciani Mm
                "id": 10100,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=10): {
                # S Margaritæ R V
                "id": 10200,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=11): {
                # S Barnabæ Ap
                "id": 10300,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostlis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=12): {
                # S Joannis a S Facundo C
                "id": 10400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Basilidi, Cyrini, Nabori atq Nazarii Mm
                    "id": 29400,
                    "mass": {"int": ["Intret in conspectu", "Sancti tui"], "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=13): {
                # S Antonii de Padua CD
                "id": 10500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=14): {
                # S Basilii Magni ECD
                "id": 10600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=15): {
                # Ss Viti, Modesti atq Crescentiæ Mm
                "id": 10700,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Multæ tribulationes", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 0,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=18): {
                # S Ephræm Syri Diaconi CD
                "id": 10800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # Ss Marci et Marcelliani Mm
                    "id": 29500,
                    "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 0,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=19): {
                # S Julianæ de Falconeriis V
                "id": 10900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Gervasii et Protasii Mm", "mass": {"int": "Loquetur Dominus "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 0,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=20): {
                # S Silverii PM
                "id": 11000,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=21): {
                # S Aloisii Gonzagæ C
                "id": 11100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Minuisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=22): {
                # S Paulini EC
                "id": 11200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sacerdotes tui", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=23): {
                # In Vigilia Nativitatis S Joannis Baptistæ
                "id": 11300,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ne timeas", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=24): {
                # In Nativitate S Joannis Baptistæ
                "id": 11400,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 0, 4, 4, 1, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "De ventre", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=25): {
                # S Gulielmi Abb
                "id": 11500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=26): {
                # S Joannis et Pauli Mm
                "id": 11600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Multæ tribulationes", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # todo Add "123/27 De IV die infra OCtava Nativitatis S Joannis Baptistae feria
            day(year=self.year, month=6, day=28): {
                # S Irinæi EM
                "id": 11800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Lex veritatis", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia Ss Petri et Pauli App
                    "id": 29600,
                    "mass": {"int": "Dicit Dominus", "glo": False, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=29): {
                # Ss Petri et Pauli App
                "id": 11900,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 2, 4, 5, 1, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Nunc scio", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=30): {
                # In Commemoratione S Pauli Apostoli
                "id": 12000,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Scio, cui credidi", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    # S Petri Ap
                    "id": 29700,
                    "mass": {"int": "", "glo": True, "cre": True, "pre": "de Apostolis"}
                },
                "com_2": {
                    # "feast": "In Octava S Joannis Baptistae"
                },
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # July
            day(year=self.year, month=7, day=1): {
                # In Festo Pretiosissimi Sanguinis DNJC
                "id": 12100,
                "rank": [2, "d I cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Redemisti nos", "glo": True, "cre": True, "pre": "de Cruce"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=2): {
                # In Visitatione BMV
                "id": 12200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve, sancta Parens", "glo": True, "cre": True, "pre": "de BMV"},
                "com_1": {
                    # Ss Processi et Martiniani Mm
                    "id": 29800,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=3): {
                # S Leonis II PC
                "id": 12300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
            # todo add "131/4 De VI die infra Octava Ss Petri et Pauli App feria
            day(year=self.year, month=7, day=5): {
                # S Antonii Mariæ Zaccaria C
                "id": 12500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sermo meus", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
            # todo add "133/6 Octava Ss Petri et Pauli App dm
            day(year=self.year, month=7, day=7): {
                # Ss Cyrilli et Methodii EeCc
                "id": 12700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sacerdotes tui", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=8): {
                # S Elisabeth R Vid
                "id": 12800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=10): {
                # Ss Septem Fratrum Mm ac Rufinæ et Secundæ VvMm
                "id": 12900,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Laudate, pueri", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=11): {
                # S Pii I PM
                "id": 13000,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=12): {
                # S Joannis Gualberti Abb
                "id": 13100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Naboris et Felicis Mm
                    "id": 29900,
                    "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=13): {
                # S Anacleti PM
                "id": 13200,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=14): {
                # S Bonaventuræ ECD
                "id": 13300,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=15): {
                # S Henrici Imp C
                "id": 13400,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=16): {
                # In Commemoratione BMV de Monte Carmelo
                "id": 13500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": " de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=17): {
                # S Alexii C
                "id": 13600,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=18): {
                # S Camilli de Lellis C
                "id": 13700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Majorem hac", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Symphorosae et Septem Filiis ejus Mm
                    "id": 30000,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=19): {
                # S Vincentii a Paulo C
                "id": 13800,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=20): {
                # S Hieronymi Æmiliani C
                "id": 13900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Effusum est", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Margaritae VM
                    "id": 30100,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=21): {
                # S Praxedis V
                "id": 14000,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=22): {
                # S Mariæ Magdalenæ Pænitentis
                "id": 14100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=23): {
                # S Apollinaris EM
                "id": 14200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Liborii EC
                    "id": 30200,
                    "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=24): {
                # In Vigilia S Jacobi Ap
                "id": 14300,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Christinae VM
                    "id": 30300,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=25): {
                # S Jacobi Ap
                "id": 14400,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    # S Christophori M
                    "id": 30400,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=26): {
                # S Annæ Matris BMV
                "id": 14500,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=27): {
                # S Pantaleonis M
                "id": 14600,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=28): {
                # Ss Nazarii et Celsi Mm, Victoris I PM, ac Innocentii I PC
                "id": 14700,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret in conspectu", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=29): {
                # S Marthæ V
                "id": 14800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Felicis II P, Simplicis, Faustinis atq Beatricae Mm
                    "id": 30500,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=30): {
                # Ss Abdon et Sennen Mm
                "id": 14900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret in conspectu", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=31): {
                # S Ignatii C
                "id": 15000,
                "rank": [14, "dm"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # August
            day(year=self.year, month=8, day=1): {
                # S Petri Ap ad Vincula
                "id": 15100,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Nunc scio vere", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    # S Pauli Ap
                    "id": 30600,
                    "mass": {"int": "", "glo": True, "cre": True, "pre": "de Apostolis"}
                },
                "com_2": {
                    # Ss Machabæis Mm
                    "id": 34700,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=2): {
                # S Alphonsi Mariæ de Ligorio ECD
                "id": 15200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Spiritus Domini", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Stephani PM
                    "id": 30700,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=3): {
                # In Inventione S Stephani Protomartyris
                "id": 15300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sederunt", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=4): {
                # S Dominici C
                "id": 15400,
                "rank": [14, "dm, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=5): {
                # In Dedicatione S Mariæ ad Nives
                "id": 15500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve, sancta parens", "glo": True, "cre": True, "pre": "De B Mariae Virginis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=6): {
                # In Transfiguratione DNJC
                "id": 15600,
                "rank": [11, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Illuxerunt", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com_1": {
                    # Ss Xysti P, Felicissimi atq Agapiti Mm
                    "id": 30800,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=7): {
                # S Cajetani C
                "id": 15700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Donati EM
                    "id": 30900,
                    "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=8): {
                # Ss Cyriaci, Largi atq Smaragdi Mm
                "id": 15800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Timete Dominum", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=9): {
                # S Joannis Mariæ Vianney C
                "id": 15900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Vigilia S Laurentii M
                    "id": 31000,
                    "mass": {"int": "Dispersit", "glo": False, "cre": False, "pre": "Communis"}
                },
                "com_2": {
                    # S Romani M
                    "id": 34800,
                    "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=10): {
                # S Laurentii M
                "id": 16000,
                "rank": [10, "d II cl"],
                "office_type": False,
                "color": "red",
                "mass": {"int": "Confessio", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=11): {
                # Ss Tiburtii et Susannæ V, Mm
                "id": 16100,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=12): {
                # S Claræ V
                "id": 16200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=13): {
                # Ss Hippolyti et Cassiani Mm
                "id": 16300,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=14): {
                # In Vigilia Assumptionis BMV
                "id": 16400,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Vultum tuum", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Eusebii C
                    "id": 31100,
                    "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {
                    "oration": "Spiritus Sancti",
                },
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=15): {
                # In Assumptione BMV
                "id": 16500,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 1, 4, 2, 1, 0),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Signum magnum", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=16): {
                # S Joachim C, Patris BMV,
                "id": 16600,
                "rank": [10, "d II cl, mtv"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dispersit", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=17): {
                # S Hyacinthi C
                "id": 16700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # Octava S Laurentii M
                    "id": 31200,
                    "mass": {"int": "Probasti", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=18): {
                # S Agapiti M
                "id": 16800,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Lætabitur", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=19): {
                # S Joannis Eudes C
                "id": 16900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=20): {
                # S Bernardi AbbD
                "id": 17000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=21): {
                # S Joannæ Franciscæ Fremiot de Chantal V
                "id": 17100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=22): {
                # In Festo Immaculati Cordis BMV
                "id": 17200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Adeamus", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # Ss Timothei, Hippolyti atq Symphoriani Mm
                    "id": 31300,
                    "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=23): {
                # S Philippi Benitii C
                "id": 17300,
                "rank": [19, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia S Bartholomæi Ap
                    "id": 31400,
                    "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=24): {
                # S Bartholomæi Ap
                "id": 17400,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=25): {
                # S Ludovici RC
                "id": 17500,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=26): {
                # S Zephrini PM
                "id": 17600,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=27): {
                # S Josephi Calasanctii C
                "id": 17700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Venite, filii", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=28): {
                # S Augustini ECD
                "id": 17800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Hermetis M
                    "id": 31500,
                    "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=29): {
                # In Decollatione S Joannis Baptistæ
                "id": 17900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Sabinae M
                    "id": 31600,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=30): {
                # S Rosæ a S Maria Limanae V
                "id": 18000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Felicis et Adaucti Mm
                    "id": 31700,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=31): {
                # S Raymundi Nonnati C
                "id": 18100,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # September
            day(year=self.year, month=9, day=1): {
                # S Ægidii Abb
                "id": 18200,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Duodecim Fratribus
                    "id": 31800,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=2): {
                # S Stephani R C
                "id": 18300,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=3): {
                # S Pii X PC
                "id": 18400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Extuli", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=5): {
                # S Laurentii Justiniani EC
                "id": 18500,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=8): {
                # In Nativitate BMV
                "id": 18600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve, sancta Parens", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Hadriani M
                    "id": 31900,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=9): {
                # S Gorgonii M
                "id": 18700,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=10): {
                # S Nicolai de Tolentino C
                "id": 18800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=11): {
                # Ss Proti et Hycinthi Mm
                "id": 18900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=12): {
                # Ssmi Nominis BMV
                "id": 19000,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Vultum tuum", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=14): {
                # In Exaltatione S Crucis
                "id": 19100,
                "rank": [14, "dm"],
                "office_type": False,
                "color": "red",
                "mass": {"int": "Nos autem", "glo": True, "cre": True, "pre": "de Cruce"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=15): {
                # Septem Dolorum BMV
                "id": 19200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Stabant", "glo": True, "seq": "Stabat Mater", "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Nicomedis M
                    "id": 32000,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=16): {
                # Ss Cornelii P et Cypriani E Mm
                "id": 19300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    # Ss Euphemiae V, Luciae atq Geminiani Mm
                    "id": 32100,
                    "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=17): {
                # In Impressione Ss Stigmatum S Francisci C
                "id": 19400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Mihi autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=18): {
                # S Josephi a Cupertino C
                "id": 19500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilectio", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=19): {
                # Ss Januarii E et Sociorum Mm
                "id": 19600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=20): {
                # Ss Eustachii et Sociorum Mm
                "id": 19700,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia S Matthæi ApEv
                    "id": 32200,
                    "mass": {"int": "Ego autem", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=21): {
                # S Matthæi ApEv
                "id": 19800,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Os justi", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=22): {
                # S Thomæ de Villanova EC
                "id": 19900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Mauritii et Sociorum Mm
                    "id": 32300,
                    "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=23): {
                # S Lini PM
                "id": 20000,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Theclae VM
                    "id": 32400,
                    "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=24): {
                # BMV de Merdece
                "id": 20100,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=26): {
                # Ss Cypriani et Justinæ Mm
                "id": 20200,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=27): {
                # Ss Cosmæ et Damiani Mm
                "id": 20300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=28): {
                # S Wenceslai Ducis M
                "id": 20400,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=29): {
                # In Dedicatione S Michaelis Arch
                "id": 20500,
                "rank": [2, "d I cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=30): {
                # S Hieronymi SCD
                "id": 20600,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # October
            day(year=self.year, month=10, day=1): {
                # S Remigii EC
                "id": 20700,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=2): {
                # Ss Angelorum Custodum
                "id": 20800,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=3): {
                # S Teresiæ a Jesu Infante V
                "id": 20900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Veni de Libano", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=4): {
                # S Francisci C
                "id": 21000,
                "rank": [14, "dm"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Mihi autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=5): {
                # Ss Placidi et Sociorum Mm
                "id": 21100,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=6): {
                # S Brunonis C
                "id": 21200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=7): {
                # Sacratissimi Rosarii BMV
                "id": 21300,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Marci PC
                    "id": 32500,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {
                    # Ss Sergii, Bacchi, Marcelli atq Apuleji MM
                    "id": 34900,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=8): {
                # S Birgittæ V
                "id": 21400,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=9): {
                # S Joannis Leonardi C
                "id": 21500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In sermonibus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Dionysii E, Rustici atq Eleutherii Mm
                    "id": 32600,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=10): {
                # S Francisci Borgiæ C
                "id": 21600,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=11): {
                # In Maternitate BMV
                "id": 21700,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ecce Virgo", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=13): {
                # S Eduardi R C
                "id": 21800,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=14): {
                # S Callisti I PM
                "id": 21900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=15): {
                # S Teresiæ V
                "id": 22000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=16): {
                # S Hedwigis V
                "id": 22100,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=17): {
                # S Margaritæ Mariæ Alacoque V
                "id": 22200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sub umbra", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=18): {
                # S Lucæ Ev
                "id": 22300,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=19): {
                # S Petri de Alcantara C
                "id": 22400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=20): {
                # S Joannis Cantii C
                "id": 22500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Miseratio hominis", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=21): {
                # S Hilarionis Abb
                "id": 22600,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Ursulae et Sociarum VM
                    "id": 32700,
                    "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=24): {
                # S Raphaelis Arch
                "id": 22700,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=25): {
                # Ss Chrysanthi et Dariæ Mm
                "id": 22800,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=26): {
                # S Evaristi PM
                "id": 22900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=27): {
                # In Vigilia Ss Simonis et Judæ App
                "id": 23000,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Intret", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=28): {
                # Ss Simonis et Judæ App
                "id": 23100,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=31): {
                # In Vigilia Omnium Sanctorum
                "id": 23200,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Judicant", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            # November
            day(year=self.year, month=11, day=1): {
                # In Festo Omnium Sanctorum
                "id": 23300,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 1, 4, 3, 1, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=2): {
                # In Commemoratione Omnium Fidelium Defunctorum
                "id": 23400,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "color": "black",
                "mass": {
                    "Ad Primam Missam": {"int": "Requiem", "glo": False, "seq": "Dies Iræ", "cre": False, "pre": "Defunctorum"},
                    "Ad Secundam Missam": {"int": "Requiem", "glo": False, "seq": "Dies Iræ", "cre": False, "pre": "Defunctorum"},
                    "Ad Tertiam Missam": {"int": "Requiem", "glo": False, "seq": "Dies Iræ", "cre": False, "pre": "Defunctorum"},
                },
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "office_type": False,
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=4): {
                # S Caroli EC
                "id": 23500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # Octavae Omnium Sanctorum
                    "id": 32800,
                    "mass": {"int": "", "glo": True, "cre": True, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
            # todo add "2371/5-7 Infra Octava Omnium Sanctorum feria
            # day(year=self.year, month=11, day=8): {
            #     # In Octava Omnium Sanctorum
            #     "rank": [16, "sd"],
            #     "nobility": (0, 0, 0, 0, 0, 0,),
            #     "office_type": False,
            #     "com": [{# Ss Quatuor Coronatis Mm", "mass": {"int": "Intret "glo": True, "cre": False, "pre": "Communis"}},],
            #     "color": "white",
            #     "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "Communis"},
            #     "matins": {
            #     "lessons": 9,
            # },
            #     "lauds": {},
            #     "prime": {},
            #     "little_hours": {},
            #     "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
            #     "compline": {},
            # },

            day(year=self.year, month=11, day=9): {
                # In Dedicatione Archibasilicæ Ssmi Salvatoris
                "id": 23700,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Terribilis", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Theodori M
                    "id": 32900,
                    "mass": {"int": "Laetabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=10): {
                # S Andreæ Avellini C
                "id": 23800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Tryphonis, Respicii atq Nymphae V Mm
                    "id": 33000,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=11): {
                # S Martini EC
                "id": 23900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Mennae M
                    "id": 33100,
                    "mass": {"int": "Laetabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=12): {
                # S Martini I PM
                "id": 24000,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=13): {
                # S Didaci C
                "id": 24100,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=14): {
                # S Josaphat EM
                "id": 24200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=15): {
                # S Alberti Magni ECD
                "id": 24300,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=16): {
                # S Gertrudis V
                "id": 24400,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=17): {
                # S Gregorii Thaumaturgi EC
                "id": 24500,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=18): {
                # In Dedicatione Basilicarum Ss Petri et Pauli App
                "id": 24600,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Terribilis", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=19): {
                # S Elisabeth V
                "id": 24700,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Pontiani PM
                    "id": 33200,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=20): {
                # S Felicis de Valois C
                "id": 24800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=21): {
                # In Præsentatione BMV
                "id": 24900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=22): {
                # S Cæciliæ VM
                "id": 25000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=23): {
                # S Clementis I PM
                "id": 25100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Dicit Dóminus", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    # S Felicitatis M
                    "id": 33300,
                    "mass": {"int": "Me exspectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=24): {
                # S Joannis a Cruce CD
                "id": 25200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Chrysogoni M
                    "id": 33400,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=25): {
                # S Catharinæ VM
                "id": 25300,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=26): {
                # S Sylvestri Abb
                "id": 25400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Petri Alexandrini EM
                    "id": 33500,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=29): {
                # In Vigilia S Andreæ Ap
                "id": 25500,
                "rank": [22, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Dominus secus", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Saturnini M
                    "id": 33600,
                    "mass": {"int": "Laetabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=30): {
                # S Andreæ Ap
                "id": 25600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
            # todo add 1259/1 feria

            # December
            day(year=self.year, month=12, day=2): {
                # S Bibianæ VM
                "id": 25800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=3): {
                # S Francisci Xaverii C
                "id": 25900,
                "rank": [14, "dm, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=4): {
                # S Petri Chrysologi ECD
                "id": 26000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Barbarae VM
                    "id": 33700,
                    "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=5): {
                # S Sabbae Abb
                "id": 26100,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=6): {
                # S Nicolai EC
                "id": 26200,
                "rank": [15, "d"],  # FIX: vigil of IC?
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia Conceptionis Immaculatæ BMV
                    "id": 33800,
                    "rank": [19, "v"],
                    "nobility": (0, 0, 0, 0, 0, 0,),
                    "office_type": False,
                    "color": "purple",
                    "mass": {"int": "Venite, audite", "glo": False, "cre": False, "pre": "Communis"},
                    "matins": {
                        "lessons": 9,
                    },
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                    "compline": {}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=7): {
                # S Ambrosii ECD
                "id": 26300,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=8): {
                # In Conceptione Immaculata BMV
                "id": 26400,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "octave": 4,
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudens gaudebo", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
            # todo add "2662/9 De II die infra Octava Concept. Immac. BMV feria
            day(year=self.year, month=12, day=10): {
                # S Melchidi PM
                "id": 26600,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=11): {
                # S Damasi I PC
                "id": 26700,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=13): {
                # S Luciæ VM
                "id": 26900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Dilexisti", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=16): {
                # S Eusebii EM
                "id": 27000,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=20): {
                # In Vigilia S Thomæ Ap
                "id": 27100,
                "rank": [22, "v"], # TODO: check the ranking of a vigil
                "nobility": (8, 2, 6, 5, 3, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=21): {
                # S Thomæ Ap
                "id": 27200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
        }

        self.data_leapyear = {
            day(year=self.year, month=2, day=23): {
                # S Petri Damiani ECD
                "id": 3500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=24): {
                # In Vigilia S Matthiæ
                "id": 27300,
                "rank": [20, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=25): {
                # S Matthiæ Ap
                "id": 3600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=27): {
                "id": False,
                # "id": 27600,
            },

            day(year=self.year, month=2, day=28): {
                # S Gabrielis a Virgine Perdolente C
                "id": 3700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Oculus Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
        }

    def leapyear(self) -> dict:
        for feast, data in self.data_leapyear.items():
            # del self.data[day(year=self.year, month=2, day=27)]
            if feast in self.data:
                if data["id"] is False:
                    del self.data[feast]
            else:
                self.data |= {feast: data}
        return self.data
