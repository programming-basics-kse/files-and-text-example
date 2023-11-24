from DataProvider import OlympicsDataProvider

DATASOURCE_PATH = "./data_source.tsv"
provider = OlympicsDataProvider(DATASOURCE_PATH)

print(len(provider.get_applicable_records()))