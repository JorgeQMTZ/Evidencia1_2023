import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")
f = sns.load_dataset("flights")
sns.relplot(x="passengers", y="month", hue="year",palette="ch:r=-.5,l=.75", data=f);
plt.title("Diagrama")

plt.show()
