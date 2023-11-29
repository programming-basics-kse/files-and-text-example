from ArgsProcessor import ArgsProcessor
from src.data.DataProvider import OlympicsDataProvider
from src.strategy.CommandContext import CommandContext
from src.strategy.CommandResolver import CommandResolver
from src.strategy.TotalCommandStrategy import TotalCommandStrategy



args = ArgsProcessor().parse()

provider = OlympicsDataProvider(args.data_path)

ctx = CommandResolver.get_command_with_params(args)

context = CommandContext(provider, ctx[0])
stats = context.execute_strategy(ctx[1])

print(stats)
