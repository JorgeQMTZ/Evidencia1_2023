#Grafico dispersion por grupo
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from random import choices

rng = np.random.RandomState(0)

x = rng.uniform(0, 1, 500)
y = 5 * x + rng.normal(0, 2, size = 500)
grupo = np.where(x < 0.4, "A", np.where(x > 0.8, "C", "B"))
grupo2 = choices(["G1", "G2"], k = 500)
x = x + rng.uniform(-0.2, 0.2, 500)

df = {'x': x, 'y': y, 'grupo': grupo, 'grupo2': grupo2}
sns.scatterplot(x = x, y = y, hue = grupo)

plt.show()