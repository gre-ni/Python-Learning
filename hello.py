def main():
    #Initialise list:
    students = []
    
    #Count from 1 to 6, exluding 6 = good for starting specifically from 1:
    for i in range(1,6):
        name = input(f"Student name {i}: ")
        
        #Adds an answer to the list:
        students.append(name)
    
    #This should adapt to length of list with students
    for i, student in enumerate(students, start=1):
        print(i, student)
    
main()

