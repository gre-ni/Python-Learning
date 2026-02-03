import csv

name = input("Name: ")
number = input("Number: ")

# Opens file, assigns to variable on the right + closes automatically after
with open("phonebook.csv", "a") as file:
    write = csv.writer(file) # Turn that file into a csv it can be written to
    write.writerow([name, number])
