from src.strategy.MedalsCommandStrategy import MedalsCommandStrategy
from src.strategy.OverallCommandStrategy import OverallCommandStrategy
from src.strategy.TotalCommandStrategy import TotalCommandStrategy


class CommandResolver:
    @staticmethod
    def get_command_with_params(args):
        if not (args.medals is None):
            country, year = args.medals
            return MedalsCommandStrategy(), (country, year)
        elif not (args.total is None):
            return TotalCommandStrategy(), args.total
        elif not (args.overall is None):
            return OverallCommandStrategy(), args.overall