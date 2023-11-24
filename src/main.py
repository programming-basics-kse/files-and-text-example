import argparse
import os

from DataProvider import OlympicsDataProvider
from StatsCollector import StatsCollector


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


path = args.data_path
if not (os.path.exists(path) and os.path.isfile(path)):
    print("Data Source path is not valid!")
    exit(1)

country, year = args.medals
if (country not in ALLOWED_COUNTRIES or
        year not in ALLOWED_YEARS):
    print("Country or Year invalid!")
    exit(1)

provider = OlympicsDataProvider(path)
StatsCollector.collect_medals_stats(provider, country, year)
