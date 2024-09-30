import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\brych\Downloads\dane_pomiarowe.csv',sep="\t")
t = np.array(df['t'])
a = np.array(df['a'])
plt.plot(t,a)
plt.show()