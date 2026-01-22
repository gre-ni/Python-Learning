class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name") # Defining my own exception and message
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        # Instance variables:
        self.name = name
        self.house = house
        self.patronus = patronus
    
    # Defining what the object will appear as when call onto as a string:
    def __str__(self):
        return f"a student {self.name} from {self.house}"
    
    # Defining my own method:
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🫎"
            case "Otter":
                return "🦭"
            case "Owl":
                return "🦉"
            case _: # Nothing recognised
                return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm()) # Return value of charm method within Student class

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    
    return Student(name, house, patronus)      
 
if __name__ == "__main__": 
    main()