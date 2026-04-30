from ordotools.tools.feast import Feast
from ordotools.tools.helpers import LiturgicalYearMarks, day, days, weeks

def existing_commemoration(feast: Feast) -> int:
    """
    Finds the number of commemorations that are already in a Feast object.
    """
    return len(feast.commemorations)

def add_commemorations(feast: Feast, first_id, second_id=None, seasonal=False):
    """
    Inserts the commemoration(s) into the Feast object.
    Expects IDs (strings or ints) which will be appended as dicts.
    """
    # Simply append to the list. 
    # Logic regarding 'addition_index' (1, 2, 3) is less relevant with a list,
    # but we verify if we are hitting limits if strict rubrics require it.
    
    # We store them as simple dicts with IDs, to be hydrated later if needed
    # or used as lookup keys.
    
    feast.commemorations.append({"id": str(first_id)})
    
    if second_id is not None:
        feast.commemorations.append({"id": str(second_id)})
        
    return feast

# [Keep fidelium and seasonal_commemorations logic largely the same]
# Just ensure when they check feast.rank_numeric, you change it to feast.rank_numericumeric

MONTH = []  # NOTE: this might not need to be a list


def fidelium(feast: Feast, bound) -> Feast:
    """
    Adds the Fidelium oration to the Feast object.
    Must be used after the seasonal commemorations are added
    """
    fidelium_or = {"id": str(99912)}
    month = feast.date.strftime("%B")
    if feast.rank_numeric == 23:  # NOTE: can rank 23 be an impeded Sunday?
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
                try:
                    feast.commemorations[1] = fidelium_or
                except IndexError:
                    feast.commemorations.append(fidelium_or)
                MONTH.append(month)

        if feast.date.strftime("%w") == 1:
            if bound.first_advent < feast.date < bound.christmas:
                pass
            elif bound.lent_begins < feast.date < bound.lent_ends:
                pass
            else:
                if feast.commemorations[1]["id"] == str(99912):
                    pass
                else:
                    feast.commemorations[1]= fidelium_or
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
                feast.rank_numeric > 15 or
                feast.rank_numeric == 12 or
                feast.rank_numeric == 9
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
