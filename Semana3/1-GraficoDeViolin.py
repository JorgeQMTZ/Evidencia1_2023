#Grafico de violin
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

rng = np.random.RandomState(1)
variable = rng.normal(0, 2, size = 50)
random.seed(1)
grupo = random.choices(["G1", "G2", "G3"], k = 50)
grupo2 = random.choices(["A", "B"], k = 50)
df = {'variable': variable, 'grupo': grupo, 'grupo2': grupo2}

sns.violinplot(x = variable)
sns.violinplot(x = "variable", data = df)

plt.show()