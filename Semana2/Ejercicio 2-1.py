#Grafica de una funcion lineal
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-11, 11)
y = 2*x + 3
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.plot(x, y)

plt.show()