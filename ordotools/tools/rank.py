from ordotools.tools.feast import Feast
import logging

def sort_criterion(e):
    return e.rank_numeric

def sorted_feasts(one: Feast, two: Feast) -> list:
    feasts = [one, two]
    feasts.sort(key=sort_criterion)
    return feasts

def commemorate(feast: Feast, commemoration: Feast) -> Feast:
    # Create a lightweight dictionary representation for the commemoration
    com_data = {
        "id": commemoration.id,
        "rank": [commemoration.rank_numeric, commemoration.rank_verbose],
        "infra_octave_name": commemoration.infra_octave_name,
        "day_in_octave": commemoration.day_in_octave,
        "color": commemoration.color,
        "mass": commemoration.mass_properties,
        "vespers": commemoration.vespers,
        "nobility": commemoration.nobility,
        "office_type": commemoration.office_type,
    }
    
    # Append to the list instead of fixed slots
    feast.commemorations.append(com_data)
    
    # If the commemorated feast had its own commemorations, absorb them?
    # Logic in old code was feast.com_2 = commemoration.com_1
    if commemoration.commemorations:
        feast.commemorations.extend(commemoration.commemorations)
        
    return feast

translated_feasts = []

def translate(feast: Feast, translated: Feast) -> Feast:
    logging.debug(f"Translating {translated.id}")
    translated_feasts.append(translated)
    return feast

def nobility(one: Feast, two: Feast, handler: int) -> Feast:
    logging.debug(f"Ranking by nobility between {one.id} and {two.id}")
    
    # New model uses List[int] for nobility
    # Iterate through available parameters safely
    length = min(len(one.nobility), len(two.nobility))
    
    for i in range(length):
        if one.nobility[i] < two.nobility[i]:
            if handler == 7:
                return commemorate(one, two)
            else:
                return translate(one, two)
        elif one.nobility[i] > two.nobility[i]:
            if handler == 7:
                return commemorate(two, one)
            else:
                return translate(two, one)
    else:
        # Fallback if identical
        return commemorate(one, two)

def rank(dynamic: Feast, static: Feast):
    # Group definitions (using numeric ranks)
    group_one = (2, 5, 6, 7, 10, 13, 11, 14, 15, 16, 18, 19, 20, 22)
    group_two = (1, 8, 12, 3, 2, 5, 6, 7, 10, 4, 13, 11, 14, 15, 16, 9, 17, 18, 19, 20, 21)
    
    one, two = None, None
    ranked = None

    d, s = dynamic.rank_numeric, static.rank_numeric

    # [Logic for filtering duplicates omitted for brevity - keep your existing logic]

    if d in group_one and d in group_two:
        if s in group_one and s not in group_two:
            pass
        elif s not in group_one and s in group_two:
            pass
        else:
            pass

    # Major ferias and vigils
    if d == 19 or s == 19:
        if d == 19:
            if "v" in dynamic.rank_verbose.lower():
                if s == 22:
                    one, two = static, dynamic
                else:
                    one, two = dynamic, static
            else:
                one, two = static, dynamic
        elif s == 19:
            if "v" in static.rank_verbose.lower():
                one, two = static, dynamic
            else:
                one, two = dynamic, static

    elif d == 21: # Our Lady Saturday
        if s < 22:
            ranked = static
    elif d == 23: # Feria
        ranked = static
    elif s == 23:
        ranked = dynamic
    elif d in group_one and s in group_two:
        one, two = dynamic, static
    else:
        one, two = static, dynamic

    if one and two:

        # Re-implement position logic using one.rank_numeric
        def get_position(feast_obj, groups):
            for count, group in enumerate(groups):
                if feast_obj.rank_numeric in group:
                    return count
            return 0 # Default

        def position_one() -> int:
            group_one_grouped = (
                (2, 5, 6, 7,),  # Duplex I classis
                (10,),          # Duplex II classis
                (13,),          # Dies Octava Communis
                (11, 14,),      # Duplex majus
                (15,),          # Duplex minus
                (16,),          # Semiduplex
                (18,),          # Dies infra Oct. communem.
                (19,),          # Vigilia
                (20,),          # Dies Octava Simplex
                (22,),          # Simplex
            )
            for count, group in enumerate(group_one_grouped):
                if one.rank_numeric in group:
                    return count
            else:
                return 0

        def position_two() -> int:
            group_two_grouped = (
                (1,),           # Dominica I classis
                (8,),           # Dominica II classis
                (12,),          # Dominica minor vel Vigilia Epiphaniæ
                (3,),           # Feria privileg., Vigilia I cl., vel dies infra Oct. I ord.
                (2, 5, 6, 7,),  # Duplex I classis
                (10,),          # Duplex II classis
                (4,),           # Dies Octava II ordinis
                (13,),          # Dies Oct. Communis vel III ordinis
                (11, 14,),      # Duplex majus
                (15,),          # Duplex minus
                (16,),          # Semiduplex
                (9,),           # Dies infra Octavam II ordinis
                (17,),          # Dies infra Octavam III ordinis
                (18,),          # Dies infra Octavam communem
                (19,),          # Feria major non privilegiata
                (20,),          # Dies Octava simplex
                (21,),          # S. Maria in Sabbato
            )
            for count, group in enumerate(group_two_grouped):
                if two.rank_numeric in group:
                    return 16 - count
            else:
                return 0

        ranking_table = (
            (0, 1, 3, 1, 3, 3, 3, 3, 3, 3, 6, 5, 8, 6, 3, 3, 6,),
            (0, 3, 3, 1, 3, 6, 3, 3, 3, 3, 6, 8, 6, 6, 3, 6, 6,),
            (0, 3, 3, 3, 3, 4, 3, 3, 3, 7, 4, 4, 4, 0, 4, 4, 4,),
            (0, 3, 3, 3, 3, 4, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4,),
            (0, 3, 3, 3, 3, 4, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4,),
            (0, 3, 3, 3, 3, 4, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,),
            (0, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 4, 4, 4,),
            (0, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 0, 0,),
            (0, 7, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 2, 0, 4, 4, 4,),
            (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4,),
        )

        ranking_result = ranking_table[position_one()][position_two()]

        if ranking_result == 1:
            ranked = one
        elif ranking_result == 2:
            ranked = two
        elif ranking_result == 3:
            ranked = commemorate(one, two)
        elif ranking_result == 4:
            ranked = commemorate(two, one)
        elif ranking_result == 5:
            ranked = translate(one, two)
        elif ranking_result == 6:
            ranked = translate(two, one)
        elif ranking_result == 7:
            ranked = nobility(one, two, ranking_result)
        elif ranking_result == 8:
            ranked = nobility(one, two, ranking_result)
        else:
            # NOTE: I believe that this occurs when we have an anticipation?
            # print(f"WARNING!! We have a problem with {one.id} occuring on {two.id}")
            # BUG: were did have sorted() here before... but I am not sure if that is what
            # we are supposed to have? maybe we defined sorted() twice...
            return sorted_feasts(one, two)

        # [Keep your existing group_one_grouped / group_two_grouped definitions]
        # [Keep your ranking_table]
        
        # position_one = get_position(one, group_one_grouped)
        # position_two = get_position(two, group_two_grouped)
        # ranking_result = ranking_table[position_one][16 - position_two if ... else ...]
        

        # ... (Ranking logic execution using commemorate/translate functions above) ...
        # pass

    if ranked is not None:
        if not translated_feasts:
            return ranked
        else:
            if ranked.rank_numeric > 16:
                for translated in translated_feasts:
                    translated.date = ranked.date
                    translated_feasts.remove(translated)
                    return rank(ranked, translated)
            else:
                return ranked
