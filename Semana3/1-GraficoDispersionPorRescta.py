#Grafico de dispersion por recta
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from random import choices

rng = np.random.RandomState(0)

x = rng.uniform(0, 1, 300)
y = 5 * x + rng.normal(0, 2, size = 300)
grupo = choices(["A", "B"], k = 300)
x = x + rng.uniform(-0.2, 0.2, 300)

df = {'x': x, 'y': y, 'grupo': grupo}
df = pd.DataFrame(data = df)
sns.regplot(x = x, y = y)

sns.regplot(x = "x", y = "y", data = df)
plt.show()