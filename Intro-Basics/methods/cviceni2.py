import math
import statistics as stat

# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru, 
# potom dolů a potom běžným Pythonovským zaokrouhlováním.

number = float(input("Give me a decimal number: "))
lower_rounded = math.floor(number)
upper_rounded = math.ceil(number)
default_rounded = round(number)

print("Rounding is as follows:\n"
      f"Lower: {lower_rounded}\n"
      f"Higher: {upper_rounded}\n"
      f"Default Python: {default_rounded}\n")


# Uvažujme vysvědčení studenta, které máme uložené jako seznam.

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

# Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru. 
# Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk, matematika a fyzika. 
# Vypočítej průměr studenta z daných předmětů s využitím modulu statistics. 
# Na začátku vytvoř prázdný seznam a následně pomocí cyklu vlož do nového seznamu známky 
# ze čtyř vyjmenovaných předmětů. 
# Nakonec použij metodu statistics.mean() k výpočtu průměru. 
# Dále zkus využít funkce, které jsou zmíněné v textu, k výpočtu nejlepší 
# a nejhorší známky z daných předmětů.

grades = []

for input in school_report:
    if input[0] in ("Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"):
        grades.append(input[1])

mean = stat.mean(grades)
        
print(f"Grades: {grades}, Mean: {mean}")

# Uvažuj data v seznamu votes, což je hlasování zaměstnanců malé firmy o tom, 
# jakou akci podniknou během jejich vánočního večírku. Použij funkce mode() ke zjištění, 
# pro jakou aktivitu hlasovalo nejvíce zaměstnanců. 
# Funkce má jeden parametr - seznam, ze kterého má určit nejčastější prvek.

votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]

print(stat.mode(votes))