# # Simple example for division by zero

try: # Code that might fail
    x = 10 / 0
except: # Code that runs if an error happens
    print("Something went wrong!")

# Write code for handling 3 simultaneous exceptions.

tokens = [100, 80, 70, 65, 50]

try: 
    players = int(input("Haw many players? "))
    difficulty = int(input("Select difficulty from 1 (easiest) to 5 (hardest): "))
    amount_assigned = round(int(tokens[difficulty - 1] / players))
    print(f"Each playes has received {amount_assigned} tokens")
    
except KeyError:
    print("Invalid difficulty level (has to be 1-5).")
    
except ZeroDivisionError:
    print("At least one player has to be playing.")    
        
except ValueError:      
    print("Input is not a number.")


# Finally is a last step which happens always.
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file.")