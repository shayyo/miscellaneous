import getopt
import sys


def parse_args():
    files = []
    output_filename = "firmware.firm"
    argument_list = sys.argv[1:]
    short_options = "ho:f:"

    try:
        arguments, values = getopt.getopt(argument_list, short_options)
    except getopt.error as err:
        print(err)
        usage()
        sys.exit(2)

    for current_argument, current_value in arguments:
        if current_argument in "-h":
            usage()
            sys.exit(2)
        elif current_argument in "-o":
            output_filename = current_value
        elif current_argument in "-f":
            files.append(current_value)


def usage():
    print("Usage: build_firmware.py -o output_filename -f file1 -f file2\n")
    sys.exit(2)


if __name__ == "__main__":
    parse_args()
