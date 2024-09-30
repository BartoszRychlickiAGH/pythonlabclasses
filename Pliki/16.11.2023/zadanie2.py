import pandas as pd
import numpy as np

t = np.linspace(-10, 10, 100)  # generuje wektor 100 liczb rzeczywistych od -10 do 10
y = t * t
data = {"t": t, "y": y}
dataframe = pd.DataFrame(data)  # tworzy pandas dataframe
dataframe.to_csv(
    "plik_testowy.csv", index=False, sep="\t"
)  # index="false" omija numerowanie wierszy w tabelce wartości w csv, nie ma czegoś takiego: 1. | 2.908 | 64638 <-- index="false" omija numerowanie wierszy
