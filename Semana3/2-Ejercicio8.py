import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid") 
a = sns.load_dataset("iris") 
b = sns.FacetGrid(a, col="species") 
b.map(plt.hist, "sepal_length");
plt.title("Diagrama")

plt.show()
