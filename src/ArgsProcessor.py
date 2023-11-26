import argparse


class ArgsProcessor:
    __parser: argparse.ArgumentParser
    __args: list[str]

    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__set_medals_args_policy()
        self.__set_total_args_policy()
        self.__set_overall_args_policy()

    def parse(self):
        args = self.__parser.parse_args()
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