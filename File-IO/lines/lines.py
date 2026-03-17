import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

lines = []

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip(" \t") # Indented comments, random spaces etc.
            if line != "\n" and line[0] != "#":
                lines.append(line)
        # print(lines)
        print(len(lines))

except (FileNotFoundError, IsADirectoryError):
    sys.exit("File does not exist")
