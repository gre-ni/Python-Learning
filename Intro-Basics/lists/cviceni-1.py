pohyby = [1200, -250, -800, 540, 721, -613, -222]

# Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])

# Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])

# Vypište kolik je všech pohybů dohromady.
print(len(pohyby))

# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(min(pohyby))
print(max(pohyby))

# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
pohyby = [1200, -250, -800, 540, 721, -613, -222]

stav = 0
for amount in pohyby:
    stav = stav + amount

print(stav)

# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
# Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. 
# Otestujte jej na seznamech různých délek.

s = [1, 2, 3, 8]

def v(list):
    total = 0
    average = 0
    for number in list:
        total = total + number
    average = total / len(list)
    return average

print(v(s))

# Postupujte obdobně jako v úložce Průměr, 
# ale tentokrát sestavte výraz pro výpočet rozpětí, tedy rozdílu mezi minimální a maximální hodnotou.

def rozpeti(list):
    minimum = min(list)
    maximum = max(list)
    return maximum - minimum

print(rozpeti(s))


# Níže máš seznam akcí, které se konaly v zasedačce jedné firmy.

akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]

# Napiš program, který zjistí následující:
# Kolik se uskutečnilo pohovorů?
# V jakých jazycích se mohou zaměstnanci firmy vzdělávat?

pocet_pohovoru = 0
jazyky = []

for event in akce:
    if "pohovor" in event:
        pocet_pohovoru += 1
    elif "jazykový kurz" in event:
        x = event.split(" - ")
        if x[1] not in jazyky:
            jazyky.append(x[1])
    
print(pocet_pohovoru)
print(jazyky)

# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

seznam_lichy = [2, 3, 4, 2, 4]
seznam_sudy = [3, 4, 5, 6, 3, 2]

def stred(list):
    x = len(list)
    # return list[int(x/2)] - Same thing, but below is a bit better way to write it:
    return list[x // 2]

print(stred(seznam_lichy))
print(stred(seznam_sudy))

# Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu.

def stred_2(list):
    x = len(list)
    if x % 2 == 0: # Is even
        return list[(x // 2) - 1]
    else:
        return list[x //2]

print(stred_2(seznam_lichy))
print(stred_2(seznam_sudy))
