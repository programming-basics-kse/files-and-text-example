from DataProvider import OlympicsDataProvider


class StatsCollector:
    @staticmethod
    def collect_medals_stats(provider: OlympicsDataProvider,
                             country_name: str,
                             olympic_year: str) -> dict[str, dict[str, int]]:
        predicate = lambda item: (item.year == olympic_year and
                                  item.noc == country_name)
        applicable_records = provider.get_applicable_records(predicate)

        results = {}

        for record in applicable_records:
            descriptor = results.get(record.name)

            if descriptor is None:
                descriptor = {"Gold": 0, "Silver": 0, "Bronze": 0}
                results[record.name] = descriptor

            descriptor[record.medal] += 1

        byMedalsTotal = lambda d: sum(d[1].values())
        sorted_data = sorted(
            results.items(),
            key=byMedalsTotal,
            reverse=True)

        return {k: v for k, v in sorted_data}

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

    @staticmethod
    def collect_total_year_stats(provider: OlympicsDataProvider,
                                 olympic_year: str) -> dict[str, dict[str, int]]:
        predicate = lambda item: item.year == olympic_year
        applicable_records = provider.get_applicable_records(predicate)

        countries = {}

        for record in applicable_records:
            descriptor = countries.get(record.noc)

            if descriptor is None:
                descriptor = {"Gold": 0, "Silver": 0, "Bronze": 0}
                countries[record.noc] = descriptor

            descriptor[record.medal] += 1

        return countries
