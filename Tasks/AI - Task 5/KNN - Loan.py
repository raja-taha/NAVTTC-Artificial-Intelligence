import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the dataset
dataset = pd.read_csv("../../Datasets/loan.csv")

print(dataset.head())

#Checking for missing values
print(dataset.isnull().sum())

#Filling Gender column by mode
dataset['Gender']=dataset['Gender'].fillna(dataset['Gender'].mode().values[0])
#Filling Married column by mode
dataset['Married']=dataset['Married'].fillna(dataset['Married'].mode().values[0])
#Filling Dependents column by mode
dataset['Dependents']=dataset['Dependents'].fillna(dataset['Dependents'].mode().values[0])
#Filling Self_Employed column by mode
dataset['Self_Employed']=dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode().values[0])
#Filling LoanAmount column by mean
dataset['LoanAmount']=dataset['LoanAmount'].fillna(dataset['LoanAmount'].mean())
#Filling Loan_Amount_Term column by mode
dataset['Loan_Amount_Term']=dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode().values[0] )
#Filling Credit_History column by mode
dataset['Credit_History']=dataset['Credit_History'].fillna(dataset['Credit_History'].mode().values[0] )

#Checking missing values after imputation
print(dataset.isna().sum())

#Dropping unnecessary columns
dataset.drop('Loan_ID', axis=1, inplace=True)

print(dataset.head())

#Number of rows and columns of train set
print(dataset.shape)

#Dataset info
print(dataset.info())

sns.countplot(y = 'Gender', hue = 'Loan_Status', data = dataset)
print(dataset['Gender'].value_counts())

sns.countplot(y= 'Married', hue= 'Loan_Status', data= dataset)
print(dataset['Married'].value_counts())

sns.countplot(y = 'Education', hue = 'Loan_Status', data = dataset)
print(dataset['Education'].value_counts())

sns.countplot(y= 'Self_Employed', hue= 'Loan_Status', data= dataset)
print(dataset['Self_Employed'].value_counts())

sns.countplot(y= 'Credit_History', hue= 'Loan_Status', data=dataset)
print(dataset['Credit_History'].value_counts())

#Converting some object data type to int
gender = {"Female": 0, "Male": 1}
yes_no = {'No' : 0,'Yes' : 1}
dependents = {'0':0,'1':1,'2':2,'3+':3}
education = {'Not Graduate' : 0, 'Graduate' : 1}
property = {'Semiurban' : 0, 'Urban' : 1,'Rural' : 2}
output = {"N": 0, "Y": 1}
dataset['Gender'] = dataset['Gender'].replace(gender)
dataset['Married'] = dataset['Married'].replace(yes_no)
dataset['Dependents'] = dataset['Dependents'].replace(dependents)
dataset['Education'] = dataset['Education'].replace(education)
dataset['Self_Employed'] = dataset['Self_Employed'].replace(yes_no)
dataset['Property_Area'] = dataset['Property_Area'].replace(property)
dataset['Loan_Status'] = dataset['Loan_Status'].replace(output)

print(dataset.head())

#Setting the value for dependent and independent variables
x = dataset.drop('Loan_Status', axis=1)
y = dataset.Loan_Status

#Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test= train_test_split(x, y, test_size= 0.25, random_state=38, stratify = y)

#Fitting the KNN model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, Y_train)

#Prediction of test set
prediction_knn = knn.predict(X_test)
#Print the predicted values
print("Prediction for test set: {}".format(prediction_knn))

#Actual value and the predicted value
a = pd.DataFrame({'Actual value': Y_test, 'Predicted value': prediction_knn})
print(a.head())

#Confusion matrix and classification report
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
matrix = confusion_matrix(Y_test, prediction_knn)
sns.heatmap(matrix, annot=True, fmt="d")
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
print(classification_report(Y_test, prediction_knn))