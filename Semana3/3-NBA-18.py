import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv").head()
sns.distplot(data['Age'])

plt.title("Dist Plot")
plt.show()