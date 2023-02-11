#Mapa de color
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(2)
data = np.random.rand(4, 6)

sns.clustermap(data)
plt.show()