import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv").head()
sns.kdeplot( data['Age'])
sns.kdeplot(data['Weight'])

plt.title("Kde Plot")
plt.show()