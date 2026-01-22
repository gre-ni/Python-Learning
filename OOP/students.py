class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name") # Defining my own exception and message
        
        # Instance variables:
        self.name = name
        self.house = house
    
    # Defining what the object will appear as when call onto as a string:
    def __str__(self):
        return f"a student {self.name} from {self.house}"

    # Getter:
    def house(self):
        return self.house
    
    # Setter: 
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        return self.house


def main():
    student = get_student()
    print(student) 

def get_student():
    name = input("Name: ")
    house = input("House: ")
    
    return Student(name, house)      
 
if __name__ == "__main__": 
    main()