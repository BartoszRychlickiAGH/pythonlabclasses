def source():
    a = float(input("Wprowadz dlugosc podstawy prostopadloscianu: "))
    h = float(input("Wprowadz wysokosc prostopadloscianu: "))
    q = float(
        input("Wprowadz gestosc materialu ,z ktorego jest wykonany prostopadloscian: ")
    )

    def objetosc(a, h):
        result = a**2 * h
        return result

    def pole(a, h):
        result = 4 * a * h + 2 * a**2
        return result

    def masa(a, h, q):
        ro = objetosc(a, h)
        masa1 = ro * q
        return masa1

    print("Objetosc prostopadloscianu: ", objetosc(a, h), "[m^3]")
    print("Pole powierzchnii prostopadloscianu: ", pole(a, h), "[m^2]")
    print("Masa prostopadloscianu: ", masa(a, h, q), "[kg]")
    res = ""
    while res != "nie":
        while res != "tak":
            res = input("Czy chcesz kontynuować działanie programu? : ")
        if res == "tak":
            source()
        elif res == "nie":
            return 0
        # sprawdzić poprawność kodu, doda zabezpieczenie anty-debil
        else:
            print("Wpisz tak lub nie. Inne odpowiedzi nie są brane pod uwage")


source()
