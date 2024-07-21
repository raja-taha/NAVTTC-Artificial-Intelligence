import pandas as pd

# data_csv = pd.read_csv('../Datasets/iris.csv')
# print(data_csv)

# data_txt = pd.read_csv('../Datasets/iris.csv', header=0, sep=',')
# print(data_txt)

# data_excel = pd.read_excel('file.xlsx', sheet_name='sheet1')

# data_json = pd.read_json('file.json')

# import sqlite3
# connection_db = sqlite3.connect('DESKTOP-VQ7BUVJ.db')
# query1 = 'SELECT * FROM ProductsTable'
# data_sql = pd.read_sql_query(query1, connection_db)
# connection_db.close()
# print(data_sql)

# import pyodbc
#
# # Define your connection details
# server = 'DESKTOP-VQ7BUVJ'
# database = 'ProductsTable'
#
# # Create a connection string using Windows Authentication
# connection_string = (
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     f'SERVER={server};'
#     f'DATABASE={database};'
#     'Trusted_Connection=yes;'
# )
#
# # Establish the connection
# try:
#     connection_db = pyodbc.connect(connection_string)
#     print("Successfully connected to the database")
#
#     # Query to select all data from ProductsTable
#     query1 = 'SELECT * FROM Products'
#
#     # Reading the data into a Pandas DataFrame
#     data_sql = pd.read_sql(query1, connection_db)
#
#     # Display the DataFrame
#     print(data_sql)
#
# except pyodbc.Error as err:
#     print(f"Error: {err}")
#
# finally:
#     # Close the connection
#     if 'connection_db' in locals():
#         connection_db.close()
#         print("SQL Server connection is closed")

import pandas as pd
from sqlalchemy import create_engine

# Define your connection details
server = 'DESKTOP-VQ7BUVJ'
database = 'ProductsTable'
driver = 'ODBC Driver 17 for SQL Server'

# Create a connection string
connection_string = f'mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Query to select all data from ProductsTable
query1 = 'SELECT * FROM Products'

# Reading the data into a Pandas DataFrame
try:
    data_sql = pd.read_sql(query1, engine)
    print("Successfully connected to the database")
    # Display the DataFrame
    print(data_sql)
except Exception as e:
    print(f"Error: {e}")

# No need to close the connection explicitly when using SQLAlchemy with pandas
