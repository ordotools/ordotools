from ordotools.tools.feast import Feast
from ordotools.tools.helpers import LiturgicalYearMarks
from ordotools.tools.helpers import day
from ordotools.tools.helpers import days
from ordotools.tools.helpers import weeks

"""
Almost Everything having to do with the ordering and assignment of
commemorations is contained in this file. The "seasonal
commemorations" are added after the commemorations of concurrance
and occurance are figured out.
"""


def existing_commemoration(feast: Feast) -> int:
    """
    Finds the number of commorations that are already in a Feast object.
    """
    if "id" in feast.com_1.keys():
        if "id" in feast.com_2.keys():
            return 2
        else:
            return 1
    else:
        return 0


# TODO: add more commemoration rules (Sundays, major ferias, etc.)
# NOTE:                 This might not be always true... ⌄
def add_commemorations(feast: Feast, first, second=None, seasonal=False):
    """
    Inserts the commemoration(s) into the Feast object.
    """
    addition_index = existing_commemoration(feast)
    if addition_index == 1:
        feast.com_2["id"] = first
    elif addition_index == 2:
        if seasonal is False:
            feast.com_3["id"] = first
    else:
        feast.com_1["id"] = first
        if second is not None:
            feast.com_2["id"] = second
    return feast


MONTH = []  # NOTE: this might not need to be a list


def fidelium(feast: Feast, bound) -> Feast:
    """
    Adds the Fidelium oration to the Feast object.
    Must be used after the seasonal commemorations are added
    """
    month = feast.date.strftime("%B")
    if feast.rank_n == 23:  # NOTE: can rank 23 be an impeded Sunday?
        if month in MONTH:
            pass
        else:
            if month == "November":
                pass
            elif (
                    bound.first_advent < feast.date < bound.christmas or
                    bound.lent_begins < feast.date < bound.lent_ends or
                    bound.easter_season_start < feast.date < bound.easter_season_end
                    ):
                pass
            else:
                feast.com_2 = {"id": 99912}
                MONTH.append(month)

        if feast.date.strftime("%w") == 1:
            if bound.first_advent < feast.date < bound.christmas:
                pass
            elif bound.lent_begins < feast.date < bound.lent_ends:
                pass
            else:
                if feast.com_2["id"] == 99912:
                    pass
                else:
                    feast.com_2 = {"id": 99912}
                    MONTH.append(month)
    return feast


def seasonal_commemorations(feasts: tuple, year: int) -> tuple:
    """
    Adds the seasonal commeorations to the Feast object. Each
    add_commemoration() must take the optional seasonal parameter
    """
    bound = LiturgicalYearMarks(year)
    processed_feasts = ()
    for feast in feasts:

        if (
                feast.rank_n > 15 or
                feast.rank_n == 12 or
                feast.rank_n == 9
                ):

            if bound.first_advent < feast.date < bound.christmas:
                feast = add_commemorations(feast, 99906, 99909, seasonal=True)

            elif feast.date < bound.lent_begins-weeks(2)-days(3):
                if feast.date > day(year, 2, 2):
                    feast = add_commemorations(feast, 99911, 99913, seasonal=True)
                else:
                    feast = add_commemorations(feast, 99907, 99909, seasonal=True)

            elif bound.lent_begins-weeks(2)-days(3) < feast.date < bound.lent_begins:
                feast = add_commemorations(feast, 99907, 99909, seasonal=True)

            elif bound.lent_begins < feast.date <= bound.lent_ends-weeks(2):
                feast = add_commemorations(feast, 99911, 99914, seasonal=True)

            elif bound.lent_ends-weeks(2) < feast.date < bound.lent_ends:
                feast = add_commemorations(feast, 99909, seasonal=True)

            elif bound.easter+days(2) < feast.date < bound.easter+days(7):
                feast = add_commemorations(feast, 99909, seasonal=True)

            elif bound.easter+days(7) < feast.date < bound.easter_season_end:
                feast = add_commemorations(feast, 99908, 99909, seasonal=True)

            elif bound.pentecost_season_start < feast.date < bound.first_advent:
                feast = add_commemorations(feast, 99911, 99913, seasonal=True)

            else:
                pass
            feast = fidelium(feast=feast, bound=bound)
        else:
            pass

        processed_feasts += (feast,)

    return processed_feasts
