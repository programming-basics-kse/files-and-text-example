from src.strategy.CommandStrategy import CommandStrategy


class CommandContext:
    def __init__(self, strategy: CommandStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: CommandStrategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)
