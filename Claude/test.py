import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
penguins = sns.load_dataset('penguins')

# Quick exploration
print("First 5 rows:")
print(penguins.head())
print("\nDataset info:")
print(penguins.info())
print("\nBasic stats:")
print(penguins.describe())

# Simple scatter plot
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.title('Penguin Bill Dimensions by Species')
plt.show()