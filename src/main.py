﻿import argparse
import os

from DataProvider import OlympicsDataProvider
from StatsCollector import StatsCollector
from DataExporter import TextFileExporter

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

parser.add_argument(
    "-output",
    type=str,
    metavar="output_path"
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

output_path = args.output
if os.path.exists(output_path):
    print("Export path is not valid!")
    exit(1)


provider = OlympicsDataProvider(path)

statsV1 = StatsCollector.collect_medals_stats(provider, country, year)
print(statsV1)

all_records = provider.get_applicable_records()
statsV2 = StatsCollector.collect_medals_stats_v2(all_records, country, year)
print(statsV2)

exporter = TextFileExporter.export(output_path, statsV1)
