import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv('../Datasets/iris2.csv')
# print(data.head())

x = data.drop('species', axis=1)
y = data['species']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

#print(x_train)

scaler = StandardScaler()
scaler.fit(x_train)

#print(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# print(x_train)
# print(x_test)

regressor = KNeighborsRegressor(n_neighbors=3)
regressor.fit(x_train, y_train)
result = regressor.predict(x_test)

# print(result)

# Calculate regression metrics
mae = mean_absolute_error(y_test, result)
mse = mean_squared_error(y_test, result)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, result)

# Print regression metrics
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R²): {r2}")
