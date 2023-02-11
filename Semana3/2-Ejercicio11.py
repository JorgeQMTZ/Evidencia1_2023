import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", color_codes=True)
a = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=a);
sns.despine(offset=10, trim=True);
plt.title("Diagrama")

plt.show()