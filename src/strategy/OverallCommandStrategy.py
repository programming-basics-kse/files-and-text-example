from src.data.DataProvider import OlympicsDataProvider
from src.strategy.CommandStrategy import CommandStrategy


class OverallCommandStrategy(CommandStrategy):
    def execute(self, provider, data):
        return self.__collect_overall_stats(provider, data)

    @staticmethod
    def __collect_overall_stats(provider: OlympicsDataProvider,
                                countries: [str]) -> [dict[str, dict[str, int]]]:
        predicate = lambda c: c.noc in countries
        countries_records = provider.get_applicable_records(predicate)

        stats = {
            noc: {item.year: 0 for item in countries_records if item.noc == noc}
            for noc in countries
        }

        for item in countries_records:
            if item.noc in countries:
                stats[item.noc][item.year] += 1

        top_year_stats = {
            noc: max(year_stats.items(), key=lambda x: x[1], default=(None, 0))
            for noc, year_stats in stats.items()
        }

        return top_year_stats