import argparse
from re import compile


def main():
    # The script will take two arguments: a regular expression ("regex") and a
    # file name ("file"). Both are mandatory
    parser = argparse.ArgumentParser()
    parser.add_argument("regex", help="A regular expression, don't forget quotes (\"\")")
    parser.add_argument("file", help="The file to search")
    args = parser.parse_args()

    # Since we are going to search in every single line of the file, we are
    # compiling our regular expression
    regex = compile(args.regex)

    # We will read all the lines of the file and put them into a list.
    # Every line in the list will be checked against our compiled regEx
    # If nothing has been found - hence an AttributeError exception is raised -
    # we will continue with the next iteration of our loop
    with open(args.file, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            match = regex.search(lines[i])
            try:
                if match.group():
                    print(f"{match.group()} in line {i + 1}")
            except AttributeError:
                continue


if __name__ == "__main__":
    main()
