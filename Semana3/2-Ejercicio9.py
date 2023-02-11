import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks") 
a = sns.load_dataset("flights") 
b = sns.PairGrid(a) 
b.map(plt.scatter);
plt.title("Diagrama")

plt.show()