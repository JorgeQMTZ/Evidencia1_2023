#Grafico por pares
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")
sns.pairplot(df)

plt.show()