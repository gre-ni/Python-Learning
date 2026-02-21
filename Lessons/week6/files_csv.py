import csv

students = []

name = input("What's your name? ")
house = input("What's your house? ")


with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})


with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]}) # I could also just append row as is here


for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} is in {student['house']}")