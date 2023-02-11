import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv")
sns.set(style = 'whitegrid')
sns.barplot(x =data["Age"])

plt.title("Bar Plot")
plt.show()