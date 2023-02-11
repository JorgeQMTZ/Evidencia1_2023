#Mapa de color
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(1)
data = np.random.rand(10, 10)

sns.heatmap(data)

plt.show()
