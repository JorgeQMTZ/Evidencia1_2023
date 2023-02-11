#Grafico de barras
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,8,10])
y = np.array([12,16,6])
x2 = np.array([6,9,11])
y2 = np.array([6,15,7])
plt.bar(x, y, align="center")
plt.bar(x2, y2, color="g", align="center")
plt.title("Gráfico de Barras")

plt.show()