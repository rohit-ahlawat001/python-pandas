# Pandas Started
import pandas as pd

df = pd.read_csv("UserData_export.csv")
# print(df)

print("printing the Top 10 reaults from the data")
print(df.head(10))
print(df.tail(10))