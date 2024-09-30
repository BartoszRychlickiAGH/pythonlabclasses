def welcome(name, surname, language="pl"):
    if language == "pl":
        print("Witaj", name, surname)
    elif language == "en":
        print("Hello", name, surname)
    elif language == "fr":
        print("Bienvenue", name, surname)
    else:
        print("")


name = input("Enter your name: ")
surname = input("Enter your surname: ")
language = input("Enter a shortcut of your native language: ")
welcome(name,surname,language)