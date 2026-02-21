students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(", ")
        
        # student = {}
        # student["name"] = name
        # student["house"] = house
        # Exactly the same but shorter:
        student = {"name": name, "house": house}
        
        students.append(student)

# Sorting list of disctionaries by key:
for student in sorted(students, key=lambda student: student["house"]): 
    print(f"{student['name']} is in {student['house']}")
        