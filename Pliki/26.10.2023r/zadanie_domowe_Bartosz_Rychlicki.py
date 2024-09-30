import math as mh
import numpy as np
import re as re

# IMPORTOWANIE POTRZEBNYCH BIBLIOTEK DO DZIAŁANIA PROGRAMU
# Zamiast tylku podfunkcji, zrobić trzy główne funkcje, które zależnie od wybranej  bryły na match casie bedą ustalać wzór na result
numbers = "\D"  # losowe liczby o  rozwinięciu dziesiętnym 1 i więcej
alfa = "A-Za-z"
key = "^[[Tt]ak] | ^[[Nn]ie] "


# SEKCJA FUNKCJI ARYTMTYCZNYCH LICZĄCYCH PARAMETRY
def Pole(var):  # POLE - dodano zabezpieczenia na input
    if var == 6:  # ELIPSOIDA
        a = input("Wprowadź długośc półosi w płaszczyźnie X w [m]: ")
        b = input("Wprowadź długośc półosi w płaszczyźnie Y w [m]: ")
        c = input("Wprowadź długośc półosi w płaszczyźnie Z w [m]: ")
        while re.match(numbers, str(a)):
            print("Podano niepoprawną wartość X: ")
            a = float(input("Wprowadź długośc półosi w płaszczyźnie X w [m]: "))
        while re.match(numbers, str(b)):
            print("Podano niepoprawną wartość Y: ")
            b = float(input("Wprowadź długośc półosi w płaszczyźnie Y w [m]: "))
        while re.match(numbers, str(c)):
            print("Podano niepoprawną wartość X: ")
            float(c=input("Wprowadź długośc półosi w płaszczyźnie Z w [m]: "))
        x = float(a)
        y = float(b)  # konwersja inputa
        z = float(c)
        result = (
            2
            * mh.pi
            * y
            * (
                y
                + (x / (1 - (x**2 / y**2)) ** 0.5)
                * np.arcos((1 - (x**2 / y**2)) ** 0.5)
            )
        )
        print("Pole powiechnii elipsoidy wynosi:", result, "[m^2]")
    elif var == 5:  # WALEC
        r = float(input("Wprowadź promień walca w [m]: "))
        h = input("Wprowadź wysokośc walca w [m]: ")
        while re.match(numbers, str(r)):
            print("Wprowadzono błędną wartość r")
            r = float(input("Wprowadź promień walca w [m]: "))

        while re.match(numbers, str(h)):
            print("Wprowadzono błędną wartość h")
            h = float(input("Wprowadź wysokość walca w [m]: "))
        result = 2 * mh.pi * r**2 + 2 * mh.pi * r * h
        print("Pole walca wynosi:", result, "[m^2]")
    elif var == 4:  # STOŻEK
        r = float(input("Wprowadź promień stożka w [m]: "))
        h = float(input("Wprowadź wysokośc stożka w [m]: "))
        while re.match(numbers, str(r)):
            print("Wprowadzono błędną wartość r")
            r = float(input("Wprowadź promień w [m]: "))

        while re.match(numbers, str(h)):
            print("Wprowadzono błędną wartość h")
            h = float(input("Wprowadź wysokość w [m]: "))
        l = (r**2 + h**2) ** 0.5
        result = mh.pi * r**2 + mh.pi * r * l
        print("Pole powierzchnii stożka wynosi:", result, "[m^2]")
    elif var == 3:  # OSTROSŁUP O PODSTAWIE PROSTOKĄTA
        a = float(input("Wprowadz długość ostrosłupa w [m]: "))
        b = float(input("Wprowadz szerokość ostrosłupa w [m]: "))
        h = float(input("Wprowadz wysokość ostrosłupa w [m]: "))
        while re.match(numbers, str(a)):
            print("Wprowadzono błędną wartość a")
            a = float(input("Wprowadz długość ostrosłupa w [m]: "))

        while re.match(numbers, str(b)):
            print("Wprowadzono błędną wartość b")
            b = float(input("Wprowadz szerokość ostrosłupa w [m]: "))
        while re.match(numbers, str(h)):
            print("Wprowadzono błędną wartość b")
            h = float(input("Wprowadz wysokość ostrosłupa w [m]: "))
        result = (
            2 * (((a / 2) ** 2 + h**2) ** 0.5) * b
            + (2 * ((b / 2) ** 2 + h**2) ** 0.5) * a
            + a * b
        )
        print("Pole powierzchnii ostrosłupa wynosi:", result, "[m^2]")
    elif var == 2:  # CZWOROŚCIAN FOREMNY
        a = float(input("Podaj dugość boku czworokąta foremnego w [m]"))
        while re.match(numbers, str(a)):
            print("Wprowadzono błędną wartość")
            a = float(input("Podaj dugość boku czworokąta foremnego w [m]"))
        result = 6 * a**2
        print(
            "Pole czworokąta foemnego o boku długości:",
            a,
            "[m]",
            "wynosi:",
            result,
            "[m^2]",
        )
    elif var == 1:  # KULA
        r = float(input("Podaj promien kuli w [m]: "))
        while re.match(numbers, str(r)):
            print("Wprowadzono błędne dane")
            r = float(input("Podaj promien kuli w [m]: "))
        result = 4 * mh.pi * r**2
        print("Pole kuli o promieniu:", r, "[m]", "wynosi:", result, "[m^2]")


def Obj(var):  # OBJĘTOŚĆ
    if var == 1:  # KULA
        r = float(input("Podaj promien kuli w m"))
        if re.match(numbers, str(r)):
            print("Wprowadzono błędne dane")
            r = float(input("Podaj promien kuli w m"))
        result = 4 / 3 * mh.pi * r**3
        print("Objetosc kuli o proieniu:", r, "[m]", "wynosi:", result, "[m^3]")
        return result
    elif var == 2:  # CZWOROŚCIAN FOREMNY
        a = float(input("Podaj dugość boku czworokąta foremnego w [m]"))
        while re.match(numbers, str(a)):
            print("Wprowadzono błędne dane!")
            a = float(input("Podaj dugość boku czworokąta foremnego w [m]"))
        result = a**3
        print(
            "Objętośc czworokątu foremnego o boku długości:",
            a,
            "[m]",
            "wynosi:",
            result,
            "[m^3]",
        )
        return result
    elif var == 3:  # OSTROSŁUP O PODSTAWIE PROSTOKĄTA
        a = float(
            input(
                "Podaj długość podstawy ostrosłupa prostego o podstawie prostokąta w [m]"
            )
        )
        b = float(
            input(
                "Podaj szerokość podstawy ostrosłupa prostego o podstawie prostokąta [m]"
            )
        )
        h = float(
            input(
                "Podaj wysokość podstawy ostrosłupa prostego o podstawie prostokąta [m]"
            )
        )
        while re.match(numbers, str(a)):
            print("Wprowadzono błędnie długość podstawy")
            a = float(
                input(
                    "Podaj długość podstawy ostrosłupa prostego o podstawie prostokąta w [m]"
                )
            )
        while re.match(numbers, str(b)):
            print("Wprowadzono błędnie szerokość podstawy")
            b = float(
                input(
                    "Podaj szerokość podstawy ostrosłupa prostego o podstawie prostokąta w [m]"
                )
            )
        while re.match(numbers, str(h)):
            print("Wprowadzono błędnie wysokość podstawy")
            h = float(
                input(
                    "Podaj wysokość podstawy ostrosłupa prostego o podstawie prostokąta w [m]"
                )
            )
        result = 1 / 3 * a * b * h
        print("Objętość wynosi:", result, "[m^3]")
        return result
    elif var == 4:  # STOŻEK
        r = float(input("Wprowadź promień stożka w [m]: "))
        h = float(input("Wprowadź wysokośc stożka w [m]: "))
        while re.match(numbers, str(r)):
            print("Wprowadzono błędnie długość promienia!")
            r = float(input("Wprowadź promień stożka w [m]: "))
        while re.match(numbers, str(h)):
            print("Wprowadzono błędnie wysokość!")
            h = float(input("Wprowadź wysokość w [m]: "))
        result = 1 / 3 * h * mh.pi * r**2
        print("Objętośc wynosi:", result, "[m^3]")
        return result
    elif var == 5:  # WALEC
        r = float(input("Wprowadź promień walca w [m]: "))
        h = float(input("Wprowadź wysokośc walca w [m]: "))
        while re.match(numbers, str(r)):
            print("Wprowadzono błędnie długość promienia!")
            r = float(input("Wprowadź promień w [m]: "))
        while re.match(numbers, str(h)):
            print("Wprowadzono błędnie wysokość!")
            h = float(input("Wprowadź wysokość w [m]: "))
        result = mh.pi * r**2 * h
        print("Objętość walca wynosi: ", result, "[m^3]")
        return result
    elif var == 6:  # ELIPSOIDA
        a = float(input("Wprowadź długośc półosi w płaszczyźnie X w [m]: "))
        b = float(input("Wprowadź długośc półosi w płaszczyźnie Y w v: "))
        c = float(input("Wprowadź długośc półosi w płaszczyźnie Z w [m]: "))
        while re.match(numbers, str(a)):
            print("Podano niepoprawną wartość X: ")
            a = input("Wprowadź długośc półosi w płaszczyźnie X w [m]: ")
        while re.match(numbers, str(b)):
            print("Podano niepoprawną wartość Y: ")
            b = input("Wprowadź długośc półosi w płaszczyźnie Y w [m]: ")
        while re.match(numbers, str(c)):
            print("Podano niepoprawną wartość X: ")
            c = input("Wprowadź długośc półosi w płaszczyźnie Z w [m]: ")
        result = 4 / 3 * mh.pi * a * b * c
        print("Objętośc elipsoidy wynosi:", result, "[m^3]")
        return result


def Masa(var):  # MASA
    if var == 6:  # ELIPSOIDA
        q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
        while re.match(numbers, str(q)):
            print("Wprowadzono błędne dane!")
            q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
        V = Obj(var)
        result = V * q
        print("masa elipsoidy wynosi:", result, "[Kg]")
    elif var == 5:  # WALEC
        q = float(input("Wprowadź gęstość walca w [Kg/m^3]: "))
        while re.match(numbers, str(q)):
            print("Wprowadzono błędne dane!")
            q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
        V = Obj(var)
        result = q * V
        print("Masa walca wynosi:", result)
    elif var == 4:  # STOŻEK
        V = Obj(var)
        q = float(input("Wprowadź gęśtośc stóżka w [kg/m^3]: "))
        while re.match(numbers, str(q)):
            print("Wprowadzono błędne dane!")
            q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
        result = V * q
        print("Masa stożka wynosi:", result, "[Kg]")
    elif var == 3:  # OSTROSŁUP O PODSTAWIE PROSTOKĄTA
        q = float(
            input("Podaj gęstość ostrosłupa prostego o podstawie prostokąta w [kg/m^3]")
        )
        V = Obj(var)
        while re.match(numbers, str(q)):
            print("Wprowadzono błędne dane!")
            q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
        result = q * V
        print("Masa ostrosłupa wynosi:", result, "[Kg]")
    elif var == 2:  # MASA CZWOROŚCIAN FOREMNY
        q = float(input("Wprowadz gęstośc czworościanu foremnego  w [kg/m^3]"))
        while re.match(numbers, str(q)):
            print("Wprowadzono błędne dane!")
            q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
        V = Obj(var)
        result = V * q
        print("Masa czworościanu foremnego wynosi:", result, "[Kg]")
    elif var == 1:  # KULA
        q = float(input("Gestosc w [kg/m^3]"))
        while re.match(numbers, str(q)):
            print("Wprowadzono błędne dane!")
            q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
        V = Obj(var)
        result = V * q
        print("Masa kuli wynosi:", result, "[Kg]")


# SEKCJA FUNKCJI GŁÓWNYCH SILNIKA PROGRAMU
def Kula(var):
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    x = re.search(alfa, a)  # sprawdza czy zmienna a zawiera się we wzorcu "alfa"
    while x == 1:
        print("Wpisano niepoprawną wartość")
        Kula(var)
    match a:
        case "Objetosc":
            Obj(var)
        case "Masa":
            Masa(var)
        case "Pole powierzchnii":
            Pole(var)
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Kula(var)


def czworoscian_foremny(var):
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    x = re.search(alfa, a)
    while x == 1:
        print("Wpisano niepoprawną wartość")
        czworoscian_foremny(var)
    match a:
        case "Objetosc":
            Obj(var)
        case "Masa":
            Masa(var)
        case "Pole powierzchnii":
            Pole(var)
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            czworoscian_foremny()


def Ostroslup(var):
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    x = re.search(alfa, a)
    while x == 1:
        print("Wpisano niepoprawną wartość")
        Ostroslup(var)
    match a:
        case "Objetosc":
            Obj(var)
        case "Masa":
            Masa(var)
        case "Pole powierzchnii":
            Pole(var)
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Ostroslup()


def Stozek(var):
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    x = re.search(alfa, a)
    while x == 1:
        print("Wpisano niepoprawną wartość")
        Stozek(var)
    match a:
        case "Objetosc":
            Obj(var)
        case "Masa":
            Masa(var)
        case "Pole powierzchnii":
            Pole(var)
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Stozek()


def Walec(var):
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    x = re.search(alfa, a)
    while x == 1:
        print("Wpisano niepoprawną wartość")
        Walec(var)
    match a:
        case "Objetosc":
            Obj(var)
        case "Masa":
            Masa(var)
        case "Pole powierzchnii":
            Pole(var)
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Walec()


def Elipsoida(var):
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    x = re.search(alfa, a)
    while x == 1:
        print("Wpisano niepoprawną wartość")
        Elipsoida(var)
    match a:
        case "Objetosc":
            Obj(var)
        case "Masa":
            Masa(var)
        case "Pole powierzchnii":
            Pole(var)
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Elipsoida()


# KONIEC


# INTERFEJS UŻYTKOWNIKA
def interfejs():
    res = "tak"
    while res == "tak" or res == "Tak":
        var = int(
            input(
                "Wybierz numer figury: \n1.Kula\n2.Czworościan foremny\n3.Ostrosłup o podstawie prostokąta\n4.Stożek\n5.Walec\n6.Elipsoida\n: "
            )
        )
        match var:
            case 1:
                Kula(var)
            case 2:
                czworoscian_foremny(var)
            case 3:
                Ostroslup(var)
            case 4:
                Stozek(var)
            case 5:
                Walec(var)
            case 6:
                Elipsoida(var)
            case _:
                print(
                    "Drogi użytkowniku wprowadziłeś niepoprawne dane!! Spróbuj ponownie!!"
                )
                interfejs()
        res = input("Czy chcesz dokonać innych obliczeń: ")
        while re.match(key, res):
            print("Wprowadzono niepoprawną odpowiedź!")
            res = input("Czy chcesz dokonać innych obliczeń: ")


interfejs()
