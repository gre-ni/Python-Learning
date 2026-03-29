students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# Filter using list comprehension:
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

# Filter using filter
def is_slytherin(s):
    return s["house"] == "Slytherin"

slytherins = filter(is_slytherin, students)
