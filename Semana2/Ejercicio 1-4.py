#Diagrama de areas
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.fill_between([1, 2, 3, 4], [1, 2, 0.5, 1.5])

plt.show()