# Pandas Started
import pandas as pd

df = pd.read_csv("UserData_export.csv")
# print(df)

# print("printing the Top 10 reaults from the data")
# print(df.head(10))

# print("Printing the bottom 10 results from the data")
# print(df.tail(10))

#Printing the data into shape that get the whole data column and the rowss

print(df.shape)  

#Print data into columns to get the column of the data and that provide the data column names

print(df.columns)