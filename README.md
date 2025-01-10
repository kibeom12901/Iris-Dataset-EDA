# Iris Dataset Exploratory Data Analysis

This project explores the famous Iris dataset using Python to uncover patterns, relationships, and insights. The Iris dataset is a classic example used in machine learning and statistics education.

---

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Results and Visualizations](#results-and-visualizations)
- [Discussion](#discussion)
- [Usage](#usage)
- [Future Work](#future-work)

---

## Introduction
The Iris dataset comprises 150 observations of iris flowers from three species: **Iris setosa**, **Iris versicolor**, and **Iris virginica**. Each observation includes four features: sepal length, sepal width, petal length, and petal width.

The goal of this project is to conduct a **comprehensive Exploratory Data Analysis (EDA)** to uncover relationships and insights in the dataset. Techniques such as data cleaning, visualization, and statistical analysis are applied.

---

## Methodology
### Data Collection
- Dataset loaded using Python's **Pandas** library.

### Data Cleaning
- **Duplicate Removal**: Using `df.drop_duplicates()`.
- **Missing Values Check**: Ensured dataset completeness using `df.isnull().sum()`.

### Statistical Summary
- Summary statistics calculated with `df.describe()`.

### Data Visualization
- **Histograms** and **Density Plots** for feature distributions.
- **Box Plots** to identify outliers and data spread.
- **Scatter Plots** and **Pair Plots** to explore feature relationships.
- **Correlation Heatmap** for visualizing feature correlations.

### Outlier Detection
- Used the **Interquartile Range (IQR)** method to detect and handle outliers.

---

## Results and Visualizations

### 1. Species Distribution
**Figure 1: Species Distribution in the Iris Dataset**  
The dataset is evenly distributed among the three species.  
<img width="420" alt="Species Distribution" src="https://github.com/user-attachments/assets/35569a74-7386-438a-9a5a-ef334c1c48ed" />

---

### 2. Feature Distributions
**Figure 2: Histograms of Feature Distributions**  
Histograms and density plots showed varying distributions for features:  
- Petal length and width: Bimodal distribution.  
- Sepal length and width: Closer to normal distribution.  
<img width="262" alt="Feature Distributions" src="https://github.com/user-attachments/assets/48a190b9-07f3-418f-b2a4-fa31055d4fdc" />

---

### 3. Pairwise Relationships
**Figure 3: Pairwise Relationships Between Features**  
Pair plots highlighted clusters that distinguish species.  
<img width="337" alt="Pairwise Relationships" src="https://github.com/user-attachments/assets/a4187723-63ae-4011-a021-cd101148a6fb" />

---

### 4. Correlation Analysis
**Figure 4: Heatmap of Feature Correlations**  
A heatmap of feature correlations identified strong relationships.  
<img width="354" alt="Correlation Analysis" src="https://github.com/user-attachments/assets/639a6c05-e5cb-441a-bbec-d6c981154269" />

---

### 5. Outlier Analysis
**Figure 5: Outlier Detection in Sepal Width**  
Outliers in sepal width were detected and removed, improving data quality.  
<img width="357" alt="Outlier Analysis" src="https://github.com/user-attachments/assets/5a4a51dc-e5cf-43d7-9521-3df78cc64530" />

---

### 6. Feature Variation by Species
**Figure 6: Box Plots of Feature Variation by Species**  
Box plots were constructed for each feature to compare distributions across the three species.  
<img width="286" alt="Feature Variation by Species" src="https://github.com/user-attachments/assets/7d9971e7-f390-4c53-8ccc-43ebdd46cfa7" />

These plots highlight significant differences between species, such as the smaller sepal widths and petal sizes of **Iris setosa** compared to the other two species, which can be crucial for classification.

---

### 7. Relationship Analysis via Scatter Plots
**Figure 7: Scatter Plots of Sepal and Petal Measurements**  
Scatter plots for sepal and petal measurements further substantiate the distinct clusters by species.  
<img width="580" alt="Relationship Analysis via Scatter Plots" src="https://github.com/user-attachments/assets/88fe8250-63a2-4886-aaea-6bdd11774ca0" />

These plots emphasize how **Iris setosa** can be easily differentiated by its small petal length and width, while **Iris virginica** and **Iris versicolor** require more nuanced separation based on a combination of dimensions.

---

## Discussion
### Key Findings
- **Iris setosa**: Easily distinguishable due to small petal dimensions.
- **Iris versicolor** and **Iris virginica**: Require more nuanced separation.

### Real-World Impact
- Useful for botany (species identification) and machine learning education.

---

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Iris-Dataset-EDA.git
   cd Iris-Dataset-EDA
