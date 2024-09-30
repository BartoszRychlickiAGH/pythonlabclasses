a = float(input("Wprowadz liczbe: "))
if a == 0 or a % 2 == 0 :
    print("Liczba jest równa zero lub parzysta")
else :
    print("Liczba jest nieparzsta lub nierówna 0")
if a == 0 and a % 2 == 0 :
    print("Liczba jest równa zero i parzysta")
else :
    print("Liczba jest nieparzsta i nierówna 0 lub nierówna 0 lub nieparzysta")
print("Prosze podac wspolcynniki w zdefiniowanej przez uzytkownika funkcji kwadratowej: ")
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))
# f(x) = 3x^2 + 5x + 6
# instrukcja warunkowa( if na delcie) - ilość miejsc zerowych
delta = ((b*b) - 4*(a*c))
if delta > 0:
    print("Funkcja posiada dwa miejsca zerowe")
    x1 = ( - b - sqrt(delta)/2*a)
    x2 = ( - b + sqrt(delta)/2*a)
    print("Miejsca zerowe: " + x1, x2)
elif delta ==0 :
    print("Funkcja possiada jedno miejce zerowe")
    x = ( - b/2*a)
    print("Miejsce zerowe: " + x )
else:
    print("Funkcja nie posiada miejsc zerowych")