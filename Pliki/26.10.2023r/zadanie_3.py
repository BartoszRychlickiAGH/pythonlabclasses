import numpy as np  # potrzebne instalacja numpy za pomocą (pip install numpy) za pomocą terminala
import math as mh

a = float(input("Podaj dlugosc pierwszego boku(a): "))
b = float(input("Podaj dlugosc drugiego boku(b): "))
c = float(input("Podaj dlugosc trzeciego boku(c): "))  # wprowadzanie danych


def calculating(a, b, c):
    f = int(mh.degrees(np.arccos((c**2 - a**2 - b**2) / (2 * a * b))) / 2)
    # kąt między a i b | (c**2 - a**2 - b**2)/(2 *a*b) = cos(f)
    g = int(mh.degrees(np.arccos((b**2 - a**2 - c**2) / (2 * a * c))) / 2)
    # kąt między a i c | (b**2 - a**2 - c**2)/(2 *a*c) = cos(g)
    h = int(mh.degrees(np.arccos((a**2 - c**2 - b**2) / (2 * b * c))) / 2)
    # kąt między c i b  | (a**2 - c**2 - b**2)/(2 *b*c) = cos(h)
    #
    # /////////////////////////////////////////////////////////////////////////////////////////
    # Do sprawdzenia konstrukcja zmiany jednostki/ wartości przy użyciu odpowiednych funkcji tygonometrycznych i cyklometrycznych
    # /////////////////////////////////////////////////////////////////////////////////////////
    output(f, g, h)


def output(f, g, h):
    print("Kąt między a i b:", f)
    print("Kąt między a i c:", g)
    print("Kąt między b i c:", h)


calculating(a, b, c)
