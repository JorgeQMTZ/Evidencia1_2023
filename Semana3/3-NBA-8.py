import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas
 
data = pandas.read_csv("nba.csv")
sns.violinplot(data['Age'])

plt.title("Violin")
plt.show()