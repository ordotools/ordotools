from datetime import datetime


class Feast:
    """
    Each feast or office is of class Feast; you could say that most of the data
    is handled by this class.

    If there are too many comments here for your taste, then too bad. I have to
    take so many breaks from this project that I really need the comments so
    that I don't waste time having to remember what everything means again.
    """

    def __init__(self, feast_date: datetime, properties: dict, lang="la"):

        # the date of the feast in datetime
        self.date = feast_date

        # chaning this to id eventually, because that is what it is
        self.id = properties["id"]

        # indictates whether the feast is a day within an octave
        self.day_in_octave = properties["day_in_octave"] if "day_in_octave" in properties.keys() else 0

        # this is a placeholder for the name setter. This is unset to make life easy
        self._name = ""

        # holds a dictionary for storing the properties temporarily
        self.feast_properties = properties

        # TODO: add the "infra_octave_name" to all octaves

        # "root" name that is given to all days within an octave
        if "infra_octave_name" in properties:
            self.infra_octave_name = properties["infra_octave_name"]
        else:
            self.infra_octave_name = ""

        # verbose rank
        self.rank_v = properties["rank"][-1]

        # numeric rank
        self.rank_n = properties["rank"][0]

        # boolean value that indicates whether a feast has an octave
        self.octave = True if "Oct" in self.rank_v else False

        # color of the office (not necessarily the color of the Mass)
        self.color = properties["color"]

        # all the parts of the Mass unique to the office
        self.mass = {}

        # honestly, not sure what this does anymore...
        if "int" in properties["mass"].keys():
            self.mass = {"Ad Missam": properties["mass"]}
        else:
            for x, y in properties["mass"].items():
                self.mass.update({x: y})

        # the "nability" value of a feast, used between feasts of the same numeric rank
        self.nobility = properties["nobility"] if "nobility" in properties.keys() else (0, 0, 0, 0, 0, 0,)

        # office of sunday, feria, proper, etc.
        self.office_type = properties["office_type"]

        # self explanatory:
        self.matins = properties["matins"]
        self.lauds = properties["lauds"]
        self.prime = properties["prime"]
        self.little_hours = properties["little_hours"]
        self.vespers = properties["vespers"]
        self.compline = properties["compline"]

        # we need two separate values for fasting and abstinence, even though they are often related
        self._fasting = False
        self._abstinence = False

        # language we are going to translate the feast into eventually
        # NOTE: this might not be needed here, might just be added expense?
        self.lang = lang

# COMMEMORATIONS ------------------------------------------------------------ #

        self._com_1 = properties["com_1"]
        self._com_2 = properties["com_2"]
        self._com_3 = properties["com_3"]

    @property
    def com_1(self):
        return self._com_1

    @com_1.setter
    def com_1(self, com: dict):
        if isinstance(com["id"], str) and "de_" in com["id"]:
            com["id"] = 99914
        self._com_3 = self._com_2
        self._com_2 = self._com_1
        self._com_1 = com

    @property
    def com_2(self):
        return self._com_2

    @com_2.setter
    def com_2(self, com: dict):
        if isinstance(com["id"], str) and "de_" in com["id"]:
            com["id"] = 99914
        self._com_3 = self._com_2
        self._com_2 = com

    @property
    def com_3(self):
        return self._com_3

    @com_3.setter
    def com_3(self, com: dict):
        if isinstance(com["id"], str) and  "de_" in com["id"]:
            com["id"] = 99914
        self._com_3 = com

    # NOTE: there might be an issue with this adding blank commemorations...
    def reset_commemorations(self):
        self._com_3 = {"id": None, "name": None, "data": None}
        self._com_2 = {"id": None, "name": None, "data": None}
        self._com_1 = {"id": None, "name": None, "data": None}

# --------------------------------------------------------------------------- #

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new: str):
        self._name = new

    @property
    def abstinence(self):
        return self._abstinence

    @abstinence.setter
    def abstinence(self, q: bool):
        self._abstinence = q

    @property
    def fasting(self):
        return self._fasting

    @fasting.setter
    def fasting(self, q: bool):
        self._fasting = q

    #
    # @property
    # def date(self):
    #     return self._date
    #
    # @date.setter
    # def date(self, d: int):
    #     self._date += days(d)

    # @property
    # def name(self):
    #     return self._name

    # @lang.setter
    # def lang(self, val):
    #     # put this in the global scope?
    #     translations = Translations()
    #     self._lang = val
    #     self._name = translations.translations()[self.id][val]
    #     if self.day_in_octave != 0:
    #         self._name = translations.octave(self._lang, self.day_in_octave, self.id)

    # @property
    # def feast_date_display(self) -> str:
    #     """ Displays the feast date for the ordo """
    #     return self.date.strftime("%d")
    #
    # def readme_date(self) -> str:
    #     """ Displays the feast date for the ordo """
    #     return self.date.strftime("%b %d")
    #
    # @property
    # # TODO: expand Preces method to provide for
    # #    1. Preces Feriales
    # #    2. Compline
    # #    3. Little Hours
    #
    # def preces(self) -> str:
    #     if self.rank_n <= 16:
    #         return ""
    #     else:
    #         return "Preces"
    #
    # @property
    # def feast(self) -> str:
    #     return self.feast_properties["feast"]

    # @property
    # def updated_properties(self) -> dict:
    #     """ Updates all values of the feast's dictionary """
    #     properties = {
    #         "id": self.id,
    #         # "feast": self.name,
    #         "rank": [self.rank_n, self.rank_v],
    #         "infra_octave_name": self.infra_octave_name,
    #         "day_in_octave": self.day_in_octave,
    #         "color": self.color,
    #         "mass": self.mass,
    #         "com_1": self.com_1 if self.com_1 is not None else {},
    #         "com_2": self.com_2 if self.com_2 is not None else {},
    #         "com_3": self.com_3 if self.com_3 is not None else {},
    #         "matins": {},
    #         "lauds": {},
    #         "prime": {},
    #         "little_hours": {},
    #         "vespers": self.vespers,
    #         "compline": {},
    #         "nobility": self.nobility,
    #         "office_type": self.office_type,
    #         "fasting": self.fasting,
    #     }
    #     return properties

    #######################
    # SPECIAL LaTeX STUFF #
    #######################

    # @property
    # def office_type2latex(self) -> str:
    #     """ returns formatted office type based on office_type key """
    #     # todo write all office types in english
    #     if self.office_type is False:
    #         off_type = 'Ord, '
    #     elif self.office_type == 'feria':
    #         off_type = 'Fer, '
    #     elif self.office_type == 'festiva':
    #         off_type = 'Festiv, '
    #     elif self.office_type == 'dominica':
    #         off_type = 'Dom, '
    #     elif self.office_type == 'ut in pr loco':
    #         off_type = 'ut in pr loco, '
    #     else:
    #         return 'ERROR!'
    #     return 'Off ' + off_type
    #
    # @property
    # def com_in_title(self) -> str:
    #     """ returns formatted commemorations in title """
    #     results = ''
    #     for x in self.com:
    #         if isinstance(x) == dict:
    #             if 'feast' in x.keys():
    #                 results += r'\textit{['+x['feast'] + r']} \\ '
    #             else:
    #                 results += ''
    #         else:
    #             results += ''
    #     return results
    #
    # def introit(self) -> list:
    #     """ Finds the Introit text for the feast """
    #     # TODO: add a methed to determine if it is a three Mass Introit or not.
    #     introit_list = []
    #     if len(self.mass.items()) == 1:
    #         if 'Ad Missam' in self.mass.keys():
    #             if type(self.mass['Ad Missam']['int']) == str:
    #                 introit_list.append(self.mass['Ad Missam']['int'])
    #             else:
    #                 # TODO: determine whether it is still pascahltime or not
    #                 # ! just for testing purposes
    #                 introit_list.append(self.mass['Ad Missam']['int'][0])
    #         else:
    #             pass
    #     else:
    #         for y in self.mass.keys():
    #             introit_list.append(self.mass[y]['int'])
    #     return introit_list
    #
    # @property
    # def translate_color(self) -> str:
    #     """ translate the color from english to latin """
    #     translations = {
    #         "white": "albus",
    #         "green": "viridis",
    #         "red": "ruber",
    #         "purple": "violaceus",
    #         "black": "niger",
    #         "pink": "rosa",
    #         "color": "void",
    #     }
    #     latin_color = translations[self.color]
    #     return latin_color
    #
    # @property
    # def translate_weekday(self) -> str:
    #     """ translate the weekday from english to latin """
    #     translations = {
    #         'Sunday': 'Dom',
    #         'Monday': 'Fer II',
    #         'Tuesday': 'Fer III',
    #         'Wednesday': 'Fer IV',
    #         'Thursday': 'Fer V',
    #         'Friday': 'Fer VI',
    #         'Saturday': 'Sabb',
    #     }
    #     # latin_weekday = translations[datetime.strptime(self.feast_date.strip(
    #     #     'tranlsated ._')+'/'+str(YEAR), '%m/%d/%Y').strftime('%A')]
    #     latin_weekday = translations[self.date.strftime('%A')]
    #     return latin_weekday
    #
    # def mass_commemorations(self) -> str:
    #     """ returns formatted and ordered mass commemorations in title """
    #     results = ''
    #     i = 2
    #     for x in self.com:
    #         if isinstance(x) == dict:
    #             if 'feast' in x.keys():
    #                 results += str(i) + r' or ' + x['feast'] + r', '
    #                 i += 1
    #             # TODO: use 'feast' data as well
    #             elif 'oration' in x.keys():
    #                 if x['oration'] == 'ad libitum':
    #                     results += str(i) + r' or ' + \
    #                         x['oration'] + r', '
    #                 else:
    #                     results += str(i) + \
    #                         r' or \textit{' + x['oration'] + r',} '
    #                 i += 1
    #             else:
    #                 pass
    #         else:
    #             pass
    #     return results
    #
    # def display_mass_as_latex(self) -> str:
    #     """ return the Mass as LaTeX code """
    #     # todo add orations
    #     latexed_mass = ''
    #     pprlast = ''
    #     status = []
    #     for y in self.mass.values():
    #         gloria = y['glo']
    #         creed = y['cre']
    #         if gloria is True and creed is True:
    #             status.append('G, C, ')
    #         elif gloria is True and creed is False:
    #             status.append('G, ')
    #         elif gloria is False and creed is True:
    #             status.append('C, ')
    #         else:
    #             status.append('')
    #     i = 0
    #     # FIX: refine this to work only for its proper Mass:
    #     if 'proper_last_gospel' in y.keys():
    #         pprlast = 'ult Evgl ' + y['proper_last_gospel'] + ', '
    #     else:
    #         pprlast = ''
    #     for x, y in self.mass.items():
    #         # TODO: use the second in the string if it is Paschaltime.
    #         latexed_mass += '\\textbf{'+x+'}: \\textit{' + \
    #             self.introit()[i] + ',} ' + \
    #             status[i]+'Pre '+y['pre'] + ', ' + \
    #             self.mass_commemorations() + ' ' + pprlast + ' '
    #         i += 1
    #     return latexed_mass
    #
    # @property
    # def display_matins_as_latex(self) -> str:
    #     """ return Matins as LaTeX code """
    #     if len(self.matins) == 0:
    #         return ""
    #     else:
    #         return r"\textbf{Ad Mat}: "
    #
    # @property
    # def display_lauds_as_latex(self) -> str:
    #     """ return Laudes as LaTeX code """
    #     if len(self.lauds) == 0:
    #         return ''
    #     else:
    #         latexed_lauds = r'\textbf{Ad Lau}: '
    #         for k in self.lauds.keys():
    #             if k == 'psalms':
    #                 # * make this a bit easier to work with
    #                 if self.lauds[k] == 'sunday':
    #                     latexed_lauds += 'Pss de Dom, '
    #                 else:
    #                     pass
    #         return latexed_lauds
    #
    # @property
    # def display_little_hours_as_latex(self) -> str:
    #     """ return the little hours as LaTeX code """
    #     if len(self.little_hours) == 0:
    #         return ''
    #     else:
    #         latexed_little_hours = r'\textbf{Ad Horas}: '
    #         for k in self.little_hours.keys():
    #             if k == 'preces_feriales':
    #                 if self.prime[k] is True:
    #                     latexed_little_hours += 'Preces feriales, '
    #                 else:
    #                     pass
    #             elif k == 'psalms':
    #                 if self.little_hours[k] == 'sunday':
    #                     latexed_little_hours += 'Pss de Dom, '
    #             else:
    #                 pass
    #         return latexed_little_hours
    #
    # @property
    # def display_prime_as_latex(self) -> str:
    #     """ return Prime as LaTeX code """
    #     if len(self.prime) == 0:
    #         return ''
    #     else:
    #         latexed_prime = r'\textbf{Ad Primam}: '
    #         for k in self.prime.keys():
    #             if k == 'four_psalms':
    #                 if self.prime[k] is True:
    #                     latexed_prime += r'4 Pss, '
    #                 else:
    #                     pass
    #             elif k == 'cap':
    #                 latexed_prime += r'\textit{' + f'{self.prime[k]},' + '} '
    #             elif k == 'v_r':
    #                 latexed_prime += r'\Vbar\ in \Rbar\ brev: ' + \
    #                     r'\textit{' + f'{self.prime[k]},' + '} '
    #             elif k == 'preces_feriales':
    #                 if self.prime[k] is True:
    #                     latexed_prime += 'Preces feriales, '
    #                 else:
    #                     pass
    #             else:
    #                 pass
    #         return latexed_prime
    #
    # @property
    # def display_vespers_as_latex(self) -> str:
    #     """ return vespers as LaTeX code """
    #     if len(self.vespers) == 0:
    #         return ""
    #     else:
    #         return r"\textbf{In Vesp}: "
    #
    # @property
    # def display_compline_as_latex(self) -> str:
    #     """ return compline as LaTeX code """
    #     if len(self.compline) == 0:
    #         return ""
    #     else:
    #         latexed_compline = r"\textbf{Ad Compl}: "
    #         for k in self.compline.keys():
    #             if k == "sunday":
    #                 if self.compline[k] is True:
    #                     latexed_compline += "Pss de Dom. "
    #                 else:
    #                     pass
    #             else:
    #                 pass
    #         return latexed_compline
