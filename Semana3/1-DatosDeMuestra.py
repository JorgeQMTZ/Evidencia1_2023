#Datos de muestra
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

rng = np.random.RandomState(7)
variable = rng.normal(0.5, 2, size = 250)
random.seed(7)
grupo = random.choices(["G1", "G2", "G3"], k = 250)
grupo2 = random.choices(["A", "B"], k = 250)
df = {'variable': variable, 'grupo': grupo, 'grupo2': grupo2}

sns.stripplot(x = variable)
sns.stripplot(x = "variable", data = df)

plt.show()
