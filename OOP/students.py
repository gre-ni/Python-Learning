class Student:
    def __init__(self, name, house):
        # Instance variables (attributes):
        self.name = name
        self.house = house
    
    # Defining what the object will appear as when called onto as a string:
    def __str__(self):
        return f"a student {self.name} from {self.house}"

    @classmethod # By definition doesn't require to get a student object first
    def get(cls): # Reference to class itself via cls
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # Instantiating through using cls
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name") # Defining my own exception and message
        self._name = name 

    # Functions which are set to go through in any case when we get or set a variable:
    # Getter:
    @property
    def house(self):
        return self._house
    
    # Setter: 
    # This will be called whenever trying to access the student.house (aka self.house) attribute within object
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = Student.get()
    print(student)    
 
if __name__ == "__main__": 
    main()