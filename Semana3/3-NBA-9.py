import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv")
sns.set(style = 'whitegrid')
sns.violinplot(x ="Age", y ="Weight",data = data)

plt.title("Violin")
plt.show()