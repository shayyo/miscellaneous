import getopt
import sys

output_filename = "firmware.firm"


def parse_args():
    files = []
    argument_list = sys.argv[1:]
    short_options = "ho:f:"

    try:
        arguments, values = getopt.getopt(argument_list, short_options)
    except getopt.error as err:
        print(err)
        usage()
        sys.exit(2)

    for flag in range(len(arguments)):
        if arguments[flag][0] in "-h":
            usage()
        if arguments[flag][0] in "-o":
            global output_filename
            output_filename = arguments[flag][1]
        if arguments[flag][0] in "-f":
            files.append(arguments[flag][1])

    add_files(files)


def add_files(files):
    print(files)
    print(output_filename)


def usage():
    print("Usage: build_firmware.py -o output_filename -f file1 -f file2\n")
    sys.exit(2)


if __name__ == "__main__":
    parse_args()

