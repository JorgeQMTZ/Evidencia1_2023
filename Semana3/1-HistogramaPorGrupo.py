#Histograma Por Grupo
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.RandomState(1)
x1 = rng.normal(0, 1, size = 500)
x2 = rng.normal(3, 1.5, size = 500)
x = np.concatenate((x1, x2), axis = 0)
grupo = np.repeat(np.array(["G1", "G2"]), [500, 500], axis = 0)
df = {'x': x, 'grupo': grupo}

df = pd.DataFrame(data = df)
sns.histplot(x = x, hue = grupo)
sns.histplot(x = "x", hue = "grupo", data = df)

plt.show()