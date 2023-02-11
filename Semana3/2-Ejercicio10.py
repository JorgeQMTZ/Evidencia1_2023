import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", color_codes=True)
a = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=a);
plt.title("Diagrama")

plt.show()