import csv

name = input("Name: ")
number = input("Number: ")

# Opens file, assigns to variable on the right + closes automatically after
with open("phonebook.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["name", "number"]) # Turn that file into a csv it can be written to
    # compared to .writer, Dict will allow me to have a header row with keys
    write.writerow({"name": name, "number": number})

