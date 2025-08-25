import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

#print(penguins.head())
#print(penguins.describe())
#print(penguins.info())
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', \
                hue='species', style='sex')
plt.show()  
