import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv")
sns.boxplot( data['Age'])
sns.boxplot(data['Weight'])
    
plt.title("Box")
plt.show()