import csv
from tabulate import tabulate
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    table = []

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
            print(table)


    except (FileNotFoundError, IsADirectoryError):
        sys.exit("File does not exist")

    print(tabulate(table, headers="firstrow", tablefmt="grid"))




if __name__ == "__main__":
    main()
