import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
sns.set(color_codes=True)
a = np.random.normal(loc=5,size=100,scale=2) 
sns.distplot(a);
plt.title("Diagrama")

plt.show()