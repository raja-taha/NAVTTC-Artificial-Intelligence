import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, average_precision_score, f1_score

# Load the dataset
data = pd.read_csv('../Datasets/breast-cancer.csv')
print(data.shape)
# print(data.head())
# print(data.columns)

# Map diagnosis to numerical values: M (malignant) = 1, B (benign) = 0
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

# Separate features and target variable
X = data.drop(['id', 'diagnosis'], axis=1)
y = data['diagnosis']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Standardize the features
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# print(X_train)
# print(X_test)

# Initialize and train the K-Nearest Neighbors classifier
gnb = GaussianNB()
model = gnb.fit(X_train, y_train)

# Predict on the test set
result = gnb.predict(X_test)

# print(result)

# Print classification report and confusion matrix
print('Classification Report: \n', classification_report(y_test, result))
print('Confusion Matrix: \n', confusion_matrix(y_test, result))
print('Accuracy: \n', accuracy_score(y_test, result))
print('Precision: \n', precision_score(y_test, result))
print('Recall: \n', recall_score(y_test, result))
print('Average Precision: \n', average_precision_score(y_test, result))
print('F1 Score: \n', f1_score(y_test, result))