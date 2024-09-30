import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

a = 20
b = -2.19
c = 6
amp = 10  # amplituda wykresu
x = np.linspace(-10, 10, 100)  # dziedzina funkcji [-10,10] generuje wykres 100 liczb
y = (
    a * x**3 + b * x**2 + c * x + amp * (np.random.rand(len(x)) - 0.5)
)  # zbiór wartości funkcji parabolicznej zamiast C jest szum


# Fitowanie funkcji
def func(x, a, b, c):
    return a * x**3 + b * x**2 + c * x  # funkcja fitująca parabolę


p0 = [1, 1]
fit_params, convariance_matrix = curve_fit(func, x, y, p0=p0)

print(
    "Parametry fitowania: \na=",
    fit_params[0],
    "\nb=",
    fit_params[1],
    "\nc=",
    fit_params[2],
)
plt.scatter(x, y)
plt.plot(x, func(x, *fit_params), "r")
plt.show()
