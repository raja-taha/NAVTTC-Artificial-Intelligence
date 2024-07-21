# pip install pandas

import pandas as pd

# Pandas Series
# a = [1, 7, 2]
# myvar = pd.Series(a, index=["x", "y", "z"])
# print(myvar)

# Pandas DataFrames
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# print(df)

# Loading and reading data from CSVs
# data = pd.read_csv('../Datasets/data.csv')
# print(data)

# Iris Dataset
# data = pd.read_csv('../Datasets/iris.csv', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'species'])
# print(data)
#
# print(data.head())
# print(data.tail())
#
# print(data['species'])
#
# print(data.iloc[0])
# print(data.iloc[-1])
# print(data.iloc[:,0])
# print(data.iloc[:,-1])
# print(data.iloc[0,1])
# print(data.iloc[0:4,3:5])