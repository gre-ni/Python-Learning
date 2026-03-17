def welcome (language, name):
    if language == "en":
        print(f"Hello {name}")
    elif language == "cz":
        print(f"Ahoj {name}")
    elif language == "fr":
        print(f"Bonjour {name}")
    else:
        print(f"Hello {name}")
        
languages = ["en", "cz", "fr"]
name = "Honza"

for language in languages:
    welcome(language, name)

