import math as mh
import numpy as np

# IMPORTOWANIE POTRZEBNYCH BIBLIOTEK DO DZIAŁANIA PROGRAMU
# Zamiast tylku podfunkcji, zrobić trzy główne funkcje, które zależnie od wybranej  bryły na match casie bedą ustalać wzór na result


# SEKCJA FUNKCJI GŁÓWNYCH SILNIKA PROGRAMU
def Kula():
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    match a:
        case "Objetosc":
            Obj_k()
        case "Masa":
            Masa_k()
        case "Pole powierzchnii":
            Pole_K()
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Kula()


def czworoscian_foremny():
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    match a:
        case "Objetosc":
            Obj_cz_f()
        case "Masa":
            Masa_cz_f()
        case "Pole powierzchnii":
            Pole_cz_f()
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            czworoscian_foremny()


def Ostroslup():
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    match a:
        case "Objetosc":
            Obj_ostr()
        case "Masa":
            Masa_ostr()
        case "Pole powierzchnii":
            Pole_ostr()
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Ostroslup()


def Stozek():
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    match a:
        case "Objetosc":
            Obj_stozek()
        case "Masa":
            Masa_stozek()
        case "Pole powierzchnii":
            Pole_stozek()
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Stozek()


def Walec():
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    match a:
        case "Objetosc":
            Obj_walec()
        case "Masa":
            Masa_walec()
        case "Pole powierzchnii":
            Pole_walec()
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Walec()


def Elipsoida():
    a = input(
        "Wybierz parametr, ktory chcesz obliczyc: \nObjetosc\nMasa\nPole powierzchnii\n:"
    )
    match a:
        case "Objetosc":
            Obj_Elpis()
        case "Masa":
            Masa_Elips()
        case "Pole powierzchnii":
            Pole_Elips()
        case _:
            print("Wybrano niepoprawny parametr. Wybierz ponownie")
            Elipsoida()


# KONIEC

# SEKCJA PODFUNKCJI


# KULA
def Masa_k():  # MASA KULI
    q = float(input("Gestosc w [kg/m^3]"))
    V = Obj_k()
    result = V * q
    print("Masa kuli wynosi:", result, "[Kg]")


def Obj_k():  # OBJĘTOŚC KULI
    r = float(input("Podaj promien kuli w m"))
    result = 4 / 3 * mh.pi * r**3
    print("Objetosc kuli o proieniu:", r, "[m]", "wynosi:", result, "[m^3]")
    return result


def Pole_K():  # POLE POWIERZCHNII KULI
    r = float(input("Podaj promien kuli w [m]: "))
    result = 4 * mh.pi * r**2
    print("Pole kuli o promieniu:", r, "[m]", "wynosi:", result, "[m^2]")


# CZWOROSCIAN FOREMNY
def Masa_cz_f():  # MASA CZWOROŚCIANU FOREMNEGO
    q = float(input("Wprowadz gęstośc czworościanu foremnego  w [kg/m^3]"))
    V = Obj_cz_f()
    result = V * q
    print("Masa czworościanu foremnego wynosi:", result, "[Kg]")


def Obj_cz_f():  # OBJĘTOŚĆ CZWOROŚCIANU FOREMNEGO
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


def Pole_cz_f():  # POLE POWIERZCHNII CZWOROŚCNIANU FOREMNEGO
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


# OSTROSŁUP PROSTU O PODSTAWIE PROSTOKĄTNEJ
def Obj_ostr():
    a = float(
        input("Podaj długość podstawy ostrosłupa prostego o podstawie prostokąta w [m]")
    )
    b = float(
        input("Podaj szerokość podstawy ostrosłupa prostego o podstawie prostokąta [m]")
    )
    h = float(
        input("Podaj wysokość podstawy ostrosłupa prostego o podstawie prostokąta [m]")
    )
    result = 1 / 3 * a * b * h
    print("Objętość wynosi:", result, "[m^3]")
    return result


def Masa_ostr():
    q = float(
        input("Podaj gęstość ostrosłupa prostego o podstawie prostokąta w [kg/m^3]")
    )
    V = Obj_ostr()
    result = q * V
    print("Masa ostrosłupa wynosi:", result, "[Kg]")


def Pole_ostr():
    a = float(input("Wprowadz długość ostrosłupa w [m]: "))
    b = float(input("Wprowadz szerokość ostrosłupa w [m]: "))
    h = float(input("Wprowadz wysokość ostrosłupa w [m]: "))
    result = (
        2 * (((a / 2) ** 2 + h**2) ** 0.5) * b
        + (2 * ((b / 2) ** 2 + h**2) ** 0.5) * a
        + a * b
    )
    print("Pole powierzchnii ostrosłupa wynosi:", result, "[m^2]")


# Stożek
def Obj_stozek():
    r = float(input("Wprowadź promień stożka w [m]: "))
    h = float(input("Wprowadź wysokośc stożka w [m]: "))
    result = 1 / 3 * h * mh.pi * r**2
    print("Objętośc wynosi:", result, "[m^3]")
    return result


def Masa_stozek():
    V = Obj_stozek()
    q = float(input("Wprowadź gęśtośc stóżka w [kg/m^3]: "))
    result = V * q
    print("Masa stożka wynosi:", result, "[Kg]")


def Pole_stozek():
    r = float(input("Wprowadź promień stożka w [m]: "))
    h = float(input("Wprowadź wysokośc stożka w [m]: "))
    l = (r**2 + h**2) ** 0.5
    result = mh.pi * r**2 + mh.pi * r * l
    print("Pole powierzchnii stożka wynosi:", result, "[m^2]")


# Walec
def Obj_walec():
    r = float(input("Wprowadź promień walca w [m]: "))
    h = float(input("Wprowadź wysokośc walca w [m]: "))
    result = mh.pi * r**2 * h
    print("Objętośc walca wynosi: ", result, "[m^3]")
    return result


def Masa_walec():
    q = float(input("Wprowadź gęstość walca w [Kg/m^3]: "))
    V = Obj_walec()
    result = q * V
    print("Masa walca wynosi: ", result, "[Kg]")


def Pole_walec():
    r = float(input("Wprowadź promień walca w [m]: "))
    h = float(input("Wprowadź wysokośc walca w [m]: "))
    result = 2 * mh.pi * r**2 + 2 * mh.pi * r * h
    print("Pole walca wynosi:", result, "[m^2]")


# Elipsoida
def Obj_Elpis():
    a = float(input("Wprowadź długośc półosi w płaszczyźnie X w [m]: "))
    b = float(input("Wprowadź długośc półosi w płaszczyźnie Y w v: "))
    c = float(input("Wprowadź długośc półosi w płaszczyźnie Z w [m]: "))
    result = 4 / 3 * mh.pi * a * b * c
    print("Objętośc elipsoidy wynosi:", result, "[m^3]")
    return result


def Masa_Elips():
    q = float(input("Wprowadź gęstość elipsoidy w [Kg/m^3]: "))
    V = Obj_Elpis()
    result = V * q
    print("masa elipsoidy wynosi:", result, "[Kg]")


def Pole_Elips():
    a = float(input("Wprowadź długośc półosi w płaszczyźnie X w [m]: "))
    b = float(input("Wprowadź długośc półosi w płaszczyźnie Y w [m]: "))
    c = float(input("Wprowadź długośc półosi w płaszczyźnie Z w [m]: "))
    result = (
        2
        * mh.pi
        * b
        * (
            b
            + (a / (1 - (a**2 / b**2)) ** 0.5)
            * np.arcos((1 - (a**2 / b**2)) ** 0.5)
        )
    )
    print("Pole powiechnii elipsoidy wynosi:", result, "[m^2]")


# KONIEC


# INTERFEJS UŻYTKOWNIKA
def interfejs():
    res = "tak"
    while res == "tak" or res == "Tak":
        a = int(
            input(
                "Wybierz numer figury: \n1.Kula\n2.Czworościan foremny\n3.Ostrosłup o podstawie prostokąta\n4.Stożek\n5.Walec\n6.Elipsoida\n: "
            )
        )
        match a:
            case 1:
                Kula()
            case 2:
                czworoscian_foremny()
            case 3:
                Ostroslup()
            case 4:
                Stozek()
            case 5:
                Walec()
            case 6:
                Elipsoida()
            case _:
                print(
                    "Drogi użytkowniku wprowadziłeś niepoprawne dane!! Spróbuj ponownie!!"
                )
                interfejs()
        res = input("Czy chcesz dokonać innych obliczeń: ")


interfejs()
