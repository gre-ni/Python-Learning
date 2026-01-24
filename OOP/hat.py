import random

class Hat:
    # For clarity, it is better to define this list here, rather than inside a function:
    # Class variable:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # Class method
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry") # Capitalised since it's a method called directly on the class