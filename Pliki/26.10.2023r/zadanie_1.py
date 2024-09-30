def przeciwprostokatna(a, b):
    c = ((a**2) + (b**2)) ** 0.5
    print("Dlugosc przeciwprostokatnej wynosi: ", c)
    return c


a = float(input("Drogi uzytkowniku wprowadz dlugosc pierwszego boku: "))
b = float(input("Drogi uzytkowniku wprowadz dlugosc drugiego boku: "))
c = przeciwprostokatna(a, b)


def obwod(a, b, c):
    result = a + b + c


def surface(a, b):
    result = a * b * 0.5
