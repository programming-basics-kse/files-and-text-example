from src.data.DataProvider import OlympicsDataProvider
from src.strategy.CommandStrategy import CommandStrategy


class TotalCommandStrategy(CommandStrategy):
    def execute(self, provider, data):
        return self.__collect_total_year_stats(provider, data)

    @staticmethod
    def __collect_total_year_stats(provider: OlympicsDataProvider,
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
