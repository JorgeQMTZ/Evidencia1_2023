#Grafico de dispersion
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

rng = np.random.RandomState(0)

x = rng.uniform(0, 1, 500)
y = 5 * x + rng.normal(0, 2, size = 500)
group = np.where(x < 0.4, "A", np.where(x > 0.8, "C", "B"))
x = x + rng.uniform(-0.2, 0.2, 500)

df = {'x': x, 'y': y, 'group': group}
sns.relplot(x = x, y = y)

plt.show()