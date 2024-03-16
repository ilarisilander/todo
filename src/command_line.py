""" Module to handle the users input arguments from the command line """

import argparse


class InputArgument:
    """ Handle the arguments from the terminal """
    def __init__(self) -> None:
        pass

    def parse_arguments(self) -> str:
        arg_parser = argparse.ArgumentParser(
            description=''' Yet another TODO application '''
        )

        argument = arg_parser.parse_args()
        return argument


if __name__ == '__main__':
    pass
