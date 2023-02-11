#Histograma por densidad
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


rng = np.random.RandomState(1)
x = rng.normal(0, 1, size = 1000)
df = {'x': x}

sns.distplot(x = x, kde = True)
rng = np.random.RandomState(1)
x = rng.normal(0, 1, size = 1000)
df = {'x': x}

sns.histplot(x = x, kde = True,
             kde_kws = {'bw_adjust': 0.5})
plt.show()