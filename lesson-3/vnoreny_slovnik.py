sklad = {"Papír": {"police": 10, "regal": 15, "pocet_kusu": 0},
         "Tužky": {"police": 15, "regal": 8, "pocet_kusu": 20},
         "Sponky": {"police": 9, "regal": 9, "pocet_kusu": 987}
         }

polozka = input("Jakou položku hledáš: ")

if polozka in sklad:

    if sklad[polozka]["pocet_kusu"] > 0:
        print(f"Položka se nachází v polici {sklad[polozka]["police"]} a regálu {sklad[polozka]["regal"]}")

    else:
        print("Tuto položku nemáme skladem")

else:
    print("Tuto položku neprodáváme")