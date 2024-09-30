import matplotlib as plt
import numpy as numpy
import csv

data1 = []
data2 = []
dataT = []
data_dict = {}

file = open(f"C:\\Users\\brych\\OneDrive\\Pulpit\\1.csv")


# ////////////////////////błąd//////////////////////////////////////// eval
def DeCodeCsv(file):
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        data_dict = dict(row[0])
        # data_dict.update(row[0])
        print(data_dict)
        data1.append(data_dict.get("Pressure"))
        data2.append(data_dict.get("Acc"))
        dataT.append(data_dict.get("time"))


# //////////////////////błąd///////////////////////////////////////////


DeCodeCsv(file)


def Display():
    print(data1)
    print()
    print(data2)
    print()
    print(dataT)


# Display()


def Acc():
    plt.plot(dataT, data1)
    plt.xlabel("Czas - t[s]")
    plt.ylabel("Przyspieszenie - a[G]")
    plt.show()


def Baro():
    plt.plot(dataT, data2)
    plt.xlabel("Czas - t[s]")
    plt.ylabel("Ciśnienie - p[Pa]")
    plt.show()


# Baro()
# Acc()
