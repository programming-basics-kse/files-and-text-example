from src.data.DataProvider import OlympicsDataProvider
from src.strategy.CommandStrategy import CommandStrategy


class CommandContext:
    def __init__(self, provider: OlympicsDataProvider, strategy: CommandStrategy):
        self.__provider = provider
        self.__strategy = strategy

    def set_strategy(self, strategy: CommandStrategy):
        self.__strategy = strategy

    def execute_strategy(self, data):
        return self.__strategy.execute(self.__provider, data)
