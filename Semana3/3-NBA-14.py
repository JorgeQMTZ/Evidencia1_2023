import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv")
 
sns.set(style = 'whitegrid')
sns.pointplot(x = "Age", y = "Weight", data = data)

plt.title("Point Plot")
plt.show()