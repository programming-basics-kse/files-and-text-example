import argparse
import os


class ArgsProcessor:
    ALLOWED_COUNTRIES = ["UKR", "USA"]
    ALLOWED_YEARS = ["2000", "2004", "2012"]

    __parser: argparse.ArgumentParser
    __args: list[str]

    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__set_medals_args_policy()
        self.__set_total_args_policy()
        self.__set_overall_args_policy()

    def parse(self):
        args = self.__parser.parse_args()

        valid_args = True
        if not (args.medals is None):
            valid_args = (self.__validate_data_path(args.data_path) and
                          self.__validate_medals_args(args.medals[0], args.medals[1]) and
                          self.__validate_output_args(args.output))
        elif not (args.total is None):
            valid_args = (self.__validate_data_path(args.data_path) and
                          self.__validate_year(args.total) and
                          self.__validate_output_args(args.output))
        elif not (args.overall is None):
            valid_args = (self.__validate_data_path(args.data_path) and
                          self.__validate_countries(args.total) and
                          self.__validate_output_args(args.output))

        if not valid_args:
            print("Invalid args")
        print(args)
        return args

    def __set_medals_args_policy(self):
        # ==================== #
        #   data_path          #
        #   -medals AUT 1976   #
        #   -output result.txt #
        # ==================== #

        self.__parser.add_argument(
            "data_path",
            type=str,
            metavar="data_path")

        self.__parser.add_argument(
            '-medals',
            nargs=2,
            metavar=("country", "year")
        )

        self.__parser.add_argument(
            "-output",
            type=str,
            metavar="output_path"
        )

    def __set_total_args_policy(self):
        # ==================== #
        #   data_path          #
        #   -total 1976        #
        # ==================== #

        self.__parser.add_argument(
            '-total',
            nargs=1,
            metavar="year"
        )

    def __set_overall_args_policy(self):
        # ==================== #
        #   data_path          #
        #   -total 1976        #
        # ==================== #

        self.__parser.add_argument(
            '-overall',
            nargs='+',
            metavar="countries"
        )

    def __validate_data_path(self, path):
        return os.path.exists(path) and os.path.isfile(path)

    def __validate_medals_args(self, country, year):
        return self.__validate_country(country) and self.__validate_year(year)

    def __validate_country(self, country):
        return country in self.ALLOWED_COUNTRIES

    def __validate_year(self, year):
        return year in self.ALLOWED_YEARS

    def __validate_output_args(self, path):
        if path is not None:
            return not os.path.exists(path)
        return True

    def __validate_countries(self, total):
        for c in total:
            if not self.__validate_country(c):
                return False

        return True
