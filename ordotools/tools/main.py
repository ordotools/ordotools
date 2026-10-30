from ordotools.tools.commemorations import seasonal_commemorations
from ordotools.tools.feast import Feast, Commemoration
# from ordotools.tools.fasting import friday_abstinence, Fasting
from ordotools.tools.helpers import days
from ordotools.tools.rank import rank
from ordotools.tools.rank import transferred_feasts as transfers
from ordotools.tools.temporal import Temporal
from ordotools.tools.repositories.feasts_repo import FeastsRepository
from ordotools.tools.repositories.translations_repo import TranslationsRepository


class LiturgicalCalendar:

    def __init__(self, year, diocese="Roman", language="la", country=""):
        self.year = year
        self.diocese = diocese
        self.language = language
        self.temporal_map = Temporal(self.year).get_temporal_calendar

    def _hydrate_feast(self, date, feast_data: dict) -> Feast:
        commemorations = []
        if feast_data["commemorations"]:
            for c in feast_data["commemorations"]:
                commemorations.append(Commemoration(
                    id=str(c["id"])
                ))
            feast_data["commemorations"] = commemorations

        return Feast(
            id=str(feast_data['id']),
            date=date,
            rank_numeric=feast_data['rank'][0],
            rank_verbose=feast_data['rank'][1],
            color=feast_data['color'],
            office_type=feast_data['office_type'],
            mass_properties=feast_data['mass_properties'],
            alt_mass_properties=feast_data['alt_mass_properties'],
            nobility=feast_data['nobility'],
            commemorations=feast_data["commemorations"],
            hours={},
            matins={}, lauds={}, prime={}, little_hours={},
            vespers={}, compline={}
        )

    def expand_octaves(self, feast: Feast) -> tuple:
        octave = ()
        for i in range(1, 8):
            new_date = feast.date + days(i)
            if "communi" in feast.rank_verbose:
                new_rank_n = 18
            else:
                new_rank_n = 18 if i < 6 else 13
            new_rank_v = "sd"

            new_feast = Feast(
                id=f"{feast.id}_oct_{i}",
                date=new_date,
                rank_numeric=new_rank_n,
                rank_verbose=new_rank_v,
                color=feast.color,
                mass_properties=feast.mass_properties,
                vespers=feast.vespers,
                nobility=feast.nobility,
                office_type=feast.office_type,
                infra_octave_name=feast.infra_octave_name,
                day_in_octave=i,
                commemorations=[]
            )
            octave += (new_feast,)
        return octave

    def find_octave(self, calendar: list) -> list:
        temporal_ids = list(self.temporal_map.values())
        calendar_map = {f.date: f for f in calendar}
        for feast in calendar:
            # if it has an octave and is not in the termporal cycle
            if feast.is_octave and feast.id not in temporal_ids:
                octave_days = self.expand_octaves(feast)
                for oct_day in octave_days:
                    if oct_day.date in calendar_map:
                        winner = rank(oct_day, calendar_map[oct_day.date])
                        calendar_map[oct_day.date] = winner
                    else:
                        calendar_map[oct_day.date] = oct_day
        return sorted(calendar_map.values(), key=lambda x: x.date)

    def build(self) -> list:
        repo = FeastsRepository()
        full_calendar_map = {}
        for date, feast_id in self.temporal_map.items():
            data = repo.get_feast(feast_id)
            if data:
                full_calendar_map[date] = self._hydrate_feast(date, data)

        def cal_merger():
            prev_date = None
            for date, existing_feast in list(full_calendar_map.items()):
                sanctoral_data_list = repo.get_feasts_for_date(
                    date.month, date.day, self.diocese
                )
                for s_data in sanctoral_data_list:
                    s_feast = self._hydrate_feast(date, s_data)
                    if prev_date is not None and date != prev_date + days(1):
                        while transfers:
                            transferred = transfers[0]
                            transfers.remove(transferred)
                            transferred.date = prev_date + days(1)
                            prev_date = date
                            yield [transferred, transferred.date]
                    prev_date = date
                    yield [s_feast, date]
        for sanctoral, date in cal_merger():
            # print(f"\r[Processing] {date}".ljust(10), end="", flush=True)
            winner = rank(dynamic=sanctoral, static=full_calendar_map[date])
            if isinstance(winner, list):
                anticipated = winner[1]
                last_feast = next(reversed(full_calendar_map.values()))
                new_last_feast = rank(
                    dynamic=anticipated,
                    static=last_feast
                )
                full_calendar_map[-1] = new_last_feast
                full_calendar_map[date] = winner[0]
            else:
                full_calendar_map[date] = winner
        repo.conn.close()

        calendar_list = sorted(
            full_calendar_map.values(), key=lambda x: x.date
        )
        calendar_list = self.find_octave(calendar_list)
        calendar_list = seasonal_commemorations(calendar_list, self.year)
        trans_repo = TranslationsRepository()

        # TODO: add the translations for the commemorations
        # TODO: call all the translations and then pull from a dictionary
        for feast in calendar_list:
            t = trans_repo.get_translation(feast.id, self.language)
            if t:
                feast.name = t
            for com in feast.commemorations:
                ct = trans_repo.get_translation(com.id, self.language)
                if ct:
                    com.name = ct

        return calendar_list
