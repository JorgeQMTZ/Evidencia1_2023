#Grafico de barras
import matplotlib.pyplot as plt
import seaborn as sns

data = ["A", "A", "B",
        "B", "B", "C"]

sns.countplot(x = data)
plt.show()