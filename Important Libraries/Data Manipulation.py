import pandas as pd

dataset = pd.read_csv('../Datasets/iris.csv')

# print(dataset.head())
#
# print(dataset.tail())
#
# print(dataset.columns)
#
# print(dataset.shape)

# dataset.drop(index=[0, 1, 2, 3, 4, 5], inplace=True)

# dataset.drop(dataset.index[6:10], axis=0, inplace=True)

threshold_value = 3.0
column = 'sepal_length'
mean = dataset[column].mean()
if mean > threshold_value:
    dataset.drop(column, axis=1, inplace=True)

print(dataset)