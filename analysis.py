import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
data_frame = pd.read_csv("Iris.csv")

# Display the first few records
print("Initial data preview:")
print(data_frame.head())

# Data dimensions
print("\nData dimensions:")
print(data_frame.shape)

# Data types and non-null information
print("\nData types and completeness:")
print(data_frame.info())

# Statistical overview
print("\nStatistical overview:")
print(data_frame.describe())

# Null values check
print("\nMissing value status:")
print(data_frame.isnull().sum())

# Removing duplicate entries
unique_species = data_frame.drop_duplicates(subset="species")
print("\nUnique species records:")
print(unique_species)

# Visualization of species distribution
sns.countplot(x='species', data=data_frame)
plt.title("Distribution of Species")
plt.savefig("distribution_species.png")
plt.close()

# Scatter plots for dimensions
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=data_frame)
plt.legend(loc='upper right')
plt.title("Comparison of Sepal Dimensions")
plt.savefig("sepal_dimensions.png")
plt.close()

sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=data_frame)
plt.legend(loc='upper right')
plt.title("Comparison of Petal Dimensions")
plt.savefig("petal_dimensions.png")
plt.close()

# All pairwise relationships
sns.pairplot(data_frame, hue='species', markers=["o", "s", "D"])
plt.savefig("all_pairwise_relationships.png")
plt.close()

# Distribution histograms
fig, ax = plt.subplots(2, 2, figsize=(12, 12))
hist_features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for i, feature in enumerate(hist_features):
    ax[i//2, i%2].hist(data_frame[feature], color='blue', bins=10)
    ax[i//2, i%2].set_title(f'Histogram of {feature}')
plt.savefig("histograms_features.png")
plt.close()

# Density plots
for feature in hist_features:
    sns.histplot(data_frame, x=feature, hue="species", element="poly", fill=True)
    plt.title(f"Density Plot of {feature}")
    plt.savefig(f"density_{feature}.png")
    plt.close()

# Correlation matrix
corr_matrix = data_frame.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png")
plt.close()

# Box plots for analysis
plt.figure(figsize=(12, 12))
for i, feature in enumerate(hist_features, start=1):
    plt.subplot(2, 2, i)
    sns.boxplot(x="species", y=feature, data=data_frame)
plt.savefig("box_plots.png")
plt.close()

# Detect and remove outliers in 'Sepal Width'
Q1 = data_frame['sepal_width'].quantile(0.25)
Q3 = data_frame['sepal_width'].quantile(0.75)
IQR = Q3 - Q1
outliers = data_frame[(data_frame['sepal_width'] < (Q1 - 1.5 * IQR)) | (data_frame['sepal_width'] > (Q3 + 1.5 * IQR))]

print("Original size:", data_frame.shape)
data_frame = data_frame[~data_frame.index.isin(outliers.index)]
print("Adjusted size:", data_frame.shape)

# Box plot after outlier adjustment
sns.boxplot(x='sepal_width', data=data_frame)
plt.title("Adjusted Sepal Width")
plt.savefig("adjusted_sepal_width.png")
plt.close()
