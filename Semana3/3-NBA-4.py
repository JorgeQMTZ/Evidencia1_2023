import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv")
sns.scatterplot(data['Age'])
sns.scatterplot(data['Weight'])

plt.title("lineas")
plt.show()