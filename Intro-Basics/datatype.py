# To find out data type in a variable:
age = 5
print (type(age))

# To refer to data type in an if statement: str, int, float
user_input = input("Enter something: ")

if type(user_input) == str:
    print("You gave me text.")
elif type(user_input) == float:
    print("A decimal number.")
elif type(user_input) == int:
    print("Whole number.")
else:
    print("I don't recognise this.")
    
# Alternative, compares variable with data type in one function:
if isinstance(user_input, str):
    print("Thank you for choosing words wisely.")
