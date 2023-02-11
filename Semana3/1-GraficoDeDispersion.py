#Grafico de dispersion
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("penguins")

sns.jointplot(data = df,
              x = "bill_length_mm",
              y = "bill_depth_mm")
plt.show()