def welcome(name, surname, language="pl"):
    match language:
        case "pl":
            print("Witaj", name, surname)
        case "en":
            print("Hello", name, surname)
        case "fr":
            print("Bienvenue", name, surname)
        case _:
            print("")


name = input("Podaj swoje imie: ")
surname = input("Podaj swoje nazwisko: ")
language = input("Podaj swój język ojczysty: ")
welcome(name, surname, language)
