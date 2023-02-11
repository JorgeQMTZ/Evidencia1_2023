#Garfico de densidad
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

rng = np.random.RandomState(4)
x = rng.normal(0, 1, size = 100)
df = {'x': x}

sns.kdeplot(x = x)
sns.kdeplot(x = "x", data = df)

plt.show()