#Grafico de cajas
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns
import random

rng = np.random.RandomState(5)
variable = rng.normal(0, 1, size = 100)
random.seed(5)
grupo = random.choices(["G1", "G2", "G3"], k = 100)
grupo2 = random.choices(["A", "B"], k = 100)
df = {'variable': variable, 'grupo': grupo, 'grupo2': grupo2}

sns.boxplot(x = variable)

sns.boxplot(x = "variable", data = df)

plt.show()