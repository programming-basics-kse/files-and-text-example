import csv
from src.data.Item import Item


class OlympicsDataProvider:
    __records: set[Item]

    def __init__(self, path: str):
        self.__records = self.__get_data(path)

    def get_applicable_records(self, predicate=lambda x: True) -> set[Item]:
        return set(filter(predicate, self.__records))

    @staticmethod
    def __get_data(path: str) -> set[Item]:

        MEDALS_INDEX = 14

        records = set()
        with open(path, 'r') as file:
            reader = csv.reader(file, delimiter="\t")
            for line in reader:

                if line[MEDALS_INDEX] == "NA":
                    continue

                records.add(Item(line))

        return records
