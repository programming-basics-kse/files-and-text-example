from ArgsProcessor import ArgsProcessor
from src.data.DataProvider import OlympicsDataProvider
from src.strategy.CommandContext import CommandContext
from src.strategy.CommandResolver import CommandResolver
from src.strategy.TotalCommandStrategy import TotalCommandStrategy

ALLOWED_COUNTRIES = ["UKR", "USA"]
ALLOWED_YEARS = ["2000", "2004", "2012"]

# path = args.data_path
# if not (os.path.exists(path) and os.path.isfile(path)):
#     print("Data Source path is not valid!")
#     exit(1)
#
# country, year = args.medals
# if (country not in ALLOWED_COUNTRIES or
#         year not in ALLOWED_YEARS):
#     print("Country or Year invalid!")
#     exit(1)
#
# output_path = args.output
# if os.path.exists(output_path):
#     print("Export path is not valid or file already exists!")
#     exit(1)

args = ArgsProcessor().parse()

provider = OlympicsDataProvider(args.data_path)

ctx = CommandResolver.get_command_with_params(args)

context = CommandContext(provider, ctx[0])
stats = context.execute_strategy(ctx[1])

print(stats)
