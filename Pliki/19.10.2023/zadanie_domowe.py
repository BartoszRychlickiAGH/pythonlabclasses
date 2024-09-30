z = "tak"


def loanCalculator(a, b, c, d):  # funkcja obliczająca rate
    R = a * ((b / 12) * (1 + b / 12) ** n) / ((1 + b / 12) ** n - 1)
    return R
    
while z == "tak":
    a = float(input("Podaj kwote kredytu w zlotowkach: "))  # wprowadzanie kwoty kredytu
    b = (
        float(input("Podaj wysokosc oprocentowania: ")) * 0.01
    )  # wprowadzanie wysokości oprocentowania kredytu
    c = float(
        input("Podaj okres w latach, na ktory zostanie udzielony kredyt: ")
    )  # okres spłacania kredytu
    d = float(
        input("Podaj wysokosc miesiecznych dochodow w zlotowkach: ")
    )  # miesięczne zarobki
    n = 12 * c  # ilość rat = okres spłacania kredytu [w latach]/12]
    R = loanCalculator(
        a, b, c, d
    )  # odwołanie do fuknkcji liczącej wykokość raty z automatycznym przydzieleniem wartości zwróconej do zmiennej
    if R < 1 / 3 * d:  # instrukcja sprawdzająca dostępnośc kredytu
        print("Kredyt jest dostepny")
        print("Miesieczna rata wynosi: ", R, " zl")
    else:
        print("Kredyt nie jest dostepny: ", R, " zl")
    z = input("Czy chcesz dokonac nowych obliczen?")  # zapytanie o kontynuacje programu
