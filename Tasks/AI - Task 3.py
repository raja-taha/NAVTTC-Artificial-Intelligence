import pandas as pd
import matplotlib.pyplot as plt

# Question 1
# data = pd.read_csv('../Datasets/data.csv')
# print(data)

# Question 1: (a)
# print(data.iloc[:3])

# Question 1: (b)
# print(data.iloc[-5:])

# Question 1: (c)
# rows, columns = data.shape
#
# print(f"Number of rows: {rows}")
# print(f"Number of columns: {columns}")

# Question 1: (d)
# Adding a new column 'temperature' with all values as 'moderate'
# data['temperature'] = 'moderate'
#
# Dropping an existing column 'wind'
# data = data.drop('wind', axis=1)
#
# print(data)

# Question 2
data = pd.read_csv('../Datasets/data2.csv')
print(data[data['score'].isnull()])

# Question 3

import pandas as pd
import matplotlib.pyplot as plt

# Load the DataFrame from the CSV file
data = pd.read_csv('../Datasets/data3.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

filtered_data = data.loc['2020-04-01':'2020-04-30']

plt.figure(figsize=(10, 6))
filtered_data['Volume'].plot(kind='bar')
plt.title('Trading Volume of Alphabet Inc. Stock (01-04-2020 to 30-04-2020)')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.show()
