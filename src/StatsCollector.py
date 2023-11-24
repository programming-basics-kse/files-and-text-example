from DataProvider import OlympicsDataProvider


class StatsCollector:
    @staticmethod
    def collect_medals_stats(provider: OlympicsDataProvider,
                             country_name: str,
                             olympic_year: str) -> dict[str, int]:
        predicate = lambda item: (item.year == olympic_year and
                                  item.noc == country_name)
        applicable_records = provider.get_applicable_records(predicate)

        medals = {
            "Gold": 0,
            "Silver": 0,
            "Bronze": 0
        }

        for record in applicable_records:
            medals[record.medal] += 1

        return medals

    @staticmethod
    def collect_medals_stats_v2(records,
                                country_name: str,
                                olympic_year: str) -> dict[str, int]:
        medals = {
            "Gold": 0,
            "Silver": 0,
            "Bronze": 0
        }

        for r in records:
            if (r.year == olympic_year
                    and r.noc == country_name):
                medals[r.medal] += 1

        return medals
