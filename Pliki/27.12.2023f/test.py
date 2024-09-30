import matplotlib as plt

data = []
for i in range(0, 10, 1):
    data.append([i, i + 2])
plt.plot(data)
plt.show()
