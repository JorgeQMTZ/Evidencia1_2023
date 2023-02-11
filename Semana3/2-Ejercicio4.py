import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")
a=pd.DataFrame({'Day':[1,2,3,4,5,6,7],'Grocery':[30,80,45,23,51,46,76],'Clothes':[13,40,34,23,54,67,98],'Utensils':[12,32,27,56,87,54,34]},index=[1,2,3,4,5,6,7]) 
g = sns.relplot(x="Day", y="Clothes", kind="line", data=a)
g.fig.autofmt_xdate()
plt.title("Diagrama")

plt.show()
