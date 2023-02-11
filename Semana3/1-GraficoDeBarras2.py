#Grafico de barras
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

rng = np.random.RandomState(0)
variable = rng.normal(20, 1, size = 50)
random.seed(0)
grupo = random.choices(["G1", "G2", "G3"], k = 50)
grupo2 = random.choices(["A", "B"], k = 50)
df = {'variable': variable, 'grupo': grupo, 'grupo2': grupo2}

sns.barplot(x = grupo, y = variable)

sns.barplot(x = "grupo", y = "variable", data = df)
plt.show()
