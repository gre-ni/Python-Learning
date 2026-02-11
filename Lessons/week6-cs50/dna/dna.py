import csv
import sys


def main():

    if len(sys.argv) != 3:
        sys.exit("You need to provide two command line arguments.")

    # Reading files:
    try:
        with open(sys.argv[1]) as file:
            database = csv.DictReader(file)
            str_list = database.fieldnames  # Getting list of column names, which are STR values
            str_list = str_list[1:]  # Removing "name", leaving only list of STRs we're testing

            # Reference for comparison:
            people = []
            for row in database:
                people.append(row)

        with open(sys.argv[2], "r") as file:
            sequence = file.read()

    except FileNotFoundError:
        sys.exit("File not found")

    # Set up a dictionary where keys are names of STRs, values are what I retrieve with longest_match function
    str_dict = {}

    for i in range(len(str_list)):
        str_dict[str_list[i]] = longest_match(sequence, str_list[i])
        # print(str_dict[str_list[i]])

    found_match = None

    for person in people:  # Iterating over dictionaries
        matches = 0  # Reset for each person
        for i in range(len(str_list)):
            if int(person[str_list[i]]) == str_dict[str_list[i]]:
                matches += 1
                if matches == len(str_list):
                    found_match = person["name"]

    if not found_match:
        print("No match")
    else:
        print(found_match)


def longest_match(sequence, subsequence):

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
