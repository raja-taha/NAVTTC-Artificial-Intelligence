import pandas as pd

data = pd.read_csv('../Datasets/iris.csv')
# print(data)

# print(data.head())
# print(data.tail())

# print(data.info())

# print(data.dropna())
# print(data.fillna("NULL"))

# print(data.drop_duplicates())

# print(data.iloc[10])

data = pd.DataFrame({
    'A1': [1, 2, 3],
    'A2': [4, 5, 6],
    'A3': [7, 8, 9],},
    index=['X', 'Y', 'Z'])

# print(data)
# print(data.loc['X'])

# print(data.loc[:,'A2'])

print(data.loc['Y', 'A2'])