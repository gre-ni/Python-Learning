import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    table = []

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            if next(reader) != ['name', 'house']:
                sys.exit(f"Could not read {sys.argv[1]}")
            for row in reader:
                cleaned_row = []

                # Separate and swap names
                names = row[0].split(", ")
                cleaned_row.append(names[1])
                cleaned_row.append(names[0])

                # House stays the same
                cleaned_row.append(row[1])

                # Store to write into file later
                table.append(cleaned_row)

        with open(sys.argv[2], "w") as file:
            writer = csv.writer(file)
            writer.writerow(["first","last","house"])
            for row in table:
                writer.writerow(row)

    except (FileNotFoundError, IsADirectoryError):
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
