from abc import ABC, abstractmethod


class CommandStrategy(ABC):
    @abstractmethod
    def execute(self, provider, data):
        pass
