import argparse

from DataProvider import OlympicsDataProvider


ALLOWED_COUNTRIES = ["UKR", "USA"]
ALLOWED_YEARS = ["2000", "2004", "2012"]

# ==================== #
#   data_path          #
#   -medals AUT 1976   #
#   -output result.txt #
# ==================== #

parser = argparse.ArgumentParser()

parser.add_argument(
    "data_path",
    type=str,
    metavar="data_path")

parser.add_argument(
    '-medals',
    required=True,
    nargs=2,
    metavar=("country", "year")
)

args = parser.parse_args()
print(args)

provider = OlympicsDataProvider(args.data_path)
print(len(provider.get_applicable_records()))
