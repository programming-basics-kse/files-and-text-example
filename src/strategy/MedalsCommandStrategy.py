from src.data.DataProvider import OlympicsDataProvider
from src.strategy.CommandStrategy import CommandStrategy


class TotalCommandStrategy(CommandStrategy):
    def execute(self, provider, data):
        return self.__collect_medals_stats(provider, data[1], data[2])

    @staticmethod
    def __collect_medals_stats(provider: OlympicsDataProvider,
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
