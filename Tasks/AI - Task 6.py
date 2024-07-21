import pandas as pd
import seaborn as sns

# iris = pd.read_csv('../Datasets/iris.csv')
iris = sns.load_dataset('iris')

iris = iris.drop('species', axis=1)

mean_values = iris.mean()
print("Mean:\n", mean_values)

median_values = iris.median()
print("Median:\n", median_values)

mode_values = iris.mode()
print("Mode:\n", mode_values)

for column in iris:
    modes = iris[column].mode()
    if len(modes) > 1:
        print(f"{column} is multimodal: {modes.tolist()}")
    else:
        print(f"{column} is unimodal: {modes[0]}")

# Calculate range for each feature
range_values = iris.max() - iris.min()
print("Range:\n", range_values)

# Calculate variance for each feature
variance_values = iris.var()
print("Variance:\n", variance_values)

# Calculate standard deviation for each feature
std_dev_values = iris.std()
print("Standard Deviation:\n", std_dev_values)

# Calculate the 25th, 50th, and 75th percentiles for each feature
percentiles = iris.quantile([0.25, 0.5, 0.75])
print("Percentiles:\n", percentiles)

# Calculate quartiles for each feature
Q1 = iris.quantile(0.25)
Q2 = iris.quantile(0.50)
Q3 = iris.quantile(0.75)

print("Q1 (25th percentile):\n", Q1)
print("Q2 (50th percentile, median):\n", Q2)
print("Q3 (75th percentile):\n", Q3)

# Calculate correlation matrix
correlation_matrix = iris.corr()
print("Correlation Matrix:\n", correlation_matrix)

# Calculate covariance matrix
covariance_matrix = iris.cov()
print("Covariance Matrix:\n", covariance_matrix)
