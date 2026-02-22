import csv 

with open("favorites.csv", "r") as file: 
    
    reader = csv.DictReader(file)
    
    counts = {}
    
    for row in reader:
        favorite = row["language"]
        if favorite not in counts:
            counts[favorite] = 0
        counts[favorite] += 1

for favorite in counts:
    print(favorite, counts[favorite])