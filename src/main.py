""" Main file of the todo application """

from command_line import InputArgument


def main():
    input_argument = InputArgument()
    parsed_args = input_argument.parse_arguments()
    print(parsed_args)


if __name__ == "__main__":
    main()
