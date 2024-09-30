import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.fft import fft
from scipy.io import wavfile


class Generator:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def Sinus(self, A, f):
        x = np.linspace(
            0, self.t1, self.t2
        )  # dziedzina(między 0, a t1, ilość odstępów o t2)
        y = A * np.sin(2 * np.pi * x * 1 / (self.t1 / f))  # równanie wykresu funkcji
        # plt.scatter(x, y)
        plt.xlabel("Częstotliwość [Hz]")
        plt.ylabel("Amplituda ")  # generowanie punktów
        plt.plot(x, y)  # generowanie tabelki x,y
        plt.show()  # wyświetlanie funkcji
        a = input("Czy chcesz zapisac program?")
        if a == "tak" or a == "Tak":
            self.Saving(x, y)
        a = input("Czy chcesz stworzyć transformate Fouriera?")
        if a == "tak" or a == "Tak":
            self.TranformataFouriera(x, y)
        a = input("Czy chcesz zapisac program w rozszerzeniu wav?")
        if a == "tak" or a == "Tak":
            self.SavingWav(x, y)

    def Square(self, A, f):
        x = np.linspace(0, self.t1, self.t2)
        y = A * np.sign(np.sin(2 * np.pi * 1 / (self.t1 / f) * x))
        plt.xlabel("Częstotliwość [Hz]")
        plt.ylabel("Amplituda ")
        plt.plot(x, y)
        plt.show()
        a = input("Czy chcesz zapisac program?")
        if a == "tak" or a == "Tak":
            self.Saving(x, y)
        a = input("Czy chcesz stworzyć transformate Fouriera?")
        if a == "tak" or a == "Tak":
            self.TranformataFouriera(x, y)
        a = input("Czy chcesz zapisac program w rozszerzeniu wav?")
        if a == "tak" or a == "Tak":
            self.SavingWav(x, y)

    def Sawtooth(self, A, f):
        x = np.linspace(0, self.t1, self.t2)
        y = 2 * A / np.pi * np.arctan(np.tan(2 * np.pi * x / 2 / (self.t1 / f)))
        plt.xlabel("Częstotliwość [Hz]")
        plt.ylabel("Amplituda ")
        plt.plot(x, y)
        plt.show()
        a = input("Czy chcesz zapisac program?")
        if a == "tak" or a == "Tak":
            self.Saving(x, y)
        a = input("Czy chcesz stworzyć transformate Fouriera?")
        if a == "tak" or a == "Tak":
            self.TranformataFouriera(x, y)
        a = input("Czy chcesz zapisac program w rozszerzeniu wav?")
        if a == "tak" or a == "Tak":
            self.SavingWav(x, y)

    def Triangle(self, A, f):
        x = np.linspace(0, self.t1, self.t2)
        y = 2 * A / np.pi * np.arcsin(np.sin(2 * np.pi * x / 1 / (self.t1 / f)))
        plt.xlabel("Częstotliwość [Hz]")
        plt.ylabel("Amplituda ")
        plt.plot(x, y)
        plt.show()
        a = input("Czy chcesz zapisac program?")
        if a == "tak" or a == "Tak":
            self.Saving(x, y)
        a = input("Czy chcesz stworzyć transformate Fouriera?")
        if a == "tak" or a == "Tak":
            self.TranformataFouriera(x, y)
        a = input("Czy chcesz zapisac program w rozszerzeniu wav?")
        if a == "tak" or a == "Tak":
            self.SavingWav(x, y)

    def WhiteNoise(self, A):
        x = np.linspace(0, self.t1, self.t2)
        y = np.random.rand(len(x)) * A  # random.rand -> tworzy liste o długości len(x)
        plt.xlabel("Częstotliwość [Hz]")
        plt.ylabel("Amplituda ")
        plt.plot(x, y)
        plt.show()
        a = input("Czy chcesz zapisac program?")
        if a == "tak" or a == "Tak":
            self.Saving(x, y)
        a = input("Czy chcesz stworzyć transformate Fouriera?")
        if a == "tak" or a == "Tak":
            self.TranformataFouriera(x, y)
        a = input("Czy chcesz zapisac program w rozszerzeniu wav?")
        if a == "tak" or a == "Tak":
            self.SavingWav(x, y)

    def Saving(self, x, y):
        data = {"x": x, "y": y}  # tworzy słownik klucz-wartość przechowujący dane
        dataframe = pd.DataFrame(data)  # tworzy pandas dataframe
        dataframe.to_csv("nazwa_pliku.csv", index=False, sep="\t")  # sep -> separator

    def SavingWav(self, x, y):
        data = {"x": x, "y": y}  # tworzy słownik klucz-wartość przechowujący dane
        dataframe = pd.DataFrame(data)  # tworzy pandas dataframe
        wavfile.write("plik_testowy.wav", self.t2, y)

    def TranformataFouriera(self, x, y):
        N = len(x)
        dt = x[1] - x[0]
        y = 2.0 / N * np.abs(fft(y)[0 : N // 2])
        x = np.fft.fftfreq(N, d=dt)[0 : N // 2]
        plt.plot(x, y)
        plt.show()
        a = input("Czy chcesz zapisac program?")
        if a == "tak" or a == "Tak":
            self.Saving(x, y)


def interfejs():
    a = float(input("Podaj amplitude: "))
    b = float(input("Podaj częstotliwość: "))
    t1 = int(
        input("Podaj do jakiego czasu ma być wyświetlany przebieg czasowy w [ms]: ")
    )

    t2 = int(input("Podaj ilośc próbek: "))
    first = Generator(t1, t2)
    g = int(
        input(
            "Wybierz przebieg czasowy: \n1. Sinusoida\n2.Przebieg prostokątny\n3.Przebieg piłokształtny\n4.Przebieg trójkątny\n5.Szum"
        )
    )
    z = 1
    while z == 1:
        match g:
            case 1:
                first.Sinus(a, b)
                z = 0
            case 2:
                first.Square(a, b)
                z = 0
            case 3:
                first.Sawtooth(a, b)
                z = 0
            case 4:
                first.Triangle(a, b)
                z = 0
            case 5:
                first.WhiteNoise(a)
                z = 0
            case _:
                print("Podano zły indeks!")
                z = 1
    x = 1
    while x == 1:
        n = input("Czy chcesz kontynuować działanie programu?")
        if n == "tak" or n == "Tak":
            interfejs()
        elif n == "Nie" or n == "nie":
            x = 0
            return 0
        else:
            print("Wprowadzono niepoprawne dane!")


interfejs()
