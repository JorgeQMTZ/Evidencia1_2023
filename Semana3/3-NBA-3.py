import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

data = pandas.read_csv("nba.csv")
sns.lineplot(data['Age'],data['Weight'], hue =data["Position"])

plt.title("lineas")
plt.show()