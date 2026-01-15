# Calculating price per night based on number of guests + choice of breakfast:
price_night = 850
price_breakfast = 120

def total_price(persons, breakfast = False):
    total_people = price_night * persons
    if breakfast is True:
        total_breakfasts = price_breakfast * persons
        return total_people + total_breakfasts
    else: 
        return total_people
    
print(total_price(1))
print(total_price(1, True))