# Importing Necessary Libraries
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris_dataset = pd.read_csv('../../Datasets/iris.csv')

# Extract features (X) and labels (y)
X = iris_dataset.iloc[:, :-1].values  # Features are all columns except the last one
y = iris_dataset.iloc[:, -1].values   # Target is the last column

# Visualize the dataset using histograms and scatter plots
# Histograms
plt.figure(figsize=(10, 6))
for i in range(X.shape[1]):
    plt.subplot(2, 2, i + 1)
    plt.hist(X[:, i], bins=20, edgecolor='k')
    plt.title(iris_dataset.columns[i])
plt.tight_layout()
plt.show()

# Scatter plots
plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'blue']
species = iris_dataset['species'].unique()
for i, color in enumerate(colors):
    subset = X[y == species[i]]
    plt.scatter(subset[:, 0], subset[:, 1], label=species[i], color=color)
plt.xlabel(iris_dataset.columns[0])
plt.ylabel(iris_dataset.columns[1])
plt.legend()
plt.show()

# Encode labels as integers
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Create and Train the KNN Classifier
kn = KNeighborsClassifier()
kn.fit(X_train, y_train)

# Make Predictions and Evaluate
prediction = kn.predict(X_test)
accuracy = kn.score(X_test, y_test)
print("ACCURACY: " + str(accuracy))

# Print Predictions and Actual Values
target_names = label_encoder.classes_
for pred, actual in zip(prediction, y_test):
    print("Prediction is " + str(target_names[pred]) + ", Actual is " + str(target_names[actual]))
