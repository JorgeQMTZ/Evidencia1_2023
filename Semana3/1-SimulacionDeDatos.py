#Simulacion De Datos
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

rng = np.random.RandomState(0)
variable = rng.normal(0, 1, size = 400)
random.seed(0)
grupo = random.choices(["G1", "G2", "G3"], k = 400)
grupo2 = random.choices(["A", "B"], k = 400)
df = {'variable': variable, 'grupo': grupo, 'grupo2': grupo2}

sns.swarmplot(x = variable)
sns.swarmplot(x = "variable", data = df)

plt.show()