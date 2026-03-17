# # Podoba slovniku - klic: hodnota
# produkt = {"nazev": "Cajova konvice",
#            "cena": 0}

# # Referencing to dictionary, I am indexing based on key:
# print(produkt["nazev"])

# # Vytvoř slovník, který reprezentuje vysvědčení. 
# # Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. 
# # Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). 
# # Vypiš obsah slovníku pomocí funkce print().

# vysvedceni = {
#     "cestina": 1,
#     "matematika": 4,
#     "dejepis": 2
# }

# print(vysvedceni)

# # Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. 
# # V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů.

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }

# sales["Noc, která mě zabila"] = 0
# sales["Vrah zavolá v deset"] += 100

# print(sales)

# # V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.

# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }

# cislo_listku = int(input("What's your number? "))

# if cislo_listku in tombola:
#     print(f"You just won {tombola[cislo_listku]}!")
# else:
#     print("Sorry you won nothing.")
    

passwords = {"Jiří": "tajne-heslo", 
             "Natálie": "jeste-tajnejsi-heslo", 
             "Klára": "nejtajnejsi-heslo"}

jmeno = input("Jak se jmenujes? ")

x = 0
if jmeno in passwords:
    while x < 3: 
        heslo = input("Rekni mi heslo: ")
        if heslo in passwords[jmeno]:
            print("Welcome!")
            break
        else:
            print("Wrong password!")
            x += 1
else:
    print("You haven't been invited")
    
