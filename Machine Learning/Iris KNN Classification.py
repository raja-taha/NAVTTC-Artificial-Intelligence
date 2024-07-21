import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('../Datasets/iris.csv')
# print(data.head())

# Separate features and target variable
X = data.drop('species', axis=1)
y = data['species']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Standardize the features
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# print(X_train)
# print(X_test)

# Initialize and train the K-Nearest Neighbors classifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

# Predict on the test set
result = classifier.predict(X_test)

# print(result)

# Print classification report and confusion matrix
print('Classification Report: \n', classification_report(y_test, result))
print('Confusion Matrix: \n', confusion_matrix(y_test, result))