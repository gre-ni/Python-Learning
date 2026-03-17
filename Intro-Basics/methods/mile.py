def mile_na_kilometry(mile, namorni=False):
    if not namorni:
        return mile * 1.609344
    else:
        return mile * 1.852
    
print(mile_na_kilometry(10))