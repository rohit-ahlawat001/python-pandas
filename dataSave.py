#Saving dictonary data into the .csv file

import pandas as pd

studentData = {
    "Name": ["Rohit", "Mohit", "Bharti", "Shivansh", "Shavgi"],
     "Age": [25,30, 29, 2, 1],
     "City": ["Noida", "Chandigarh", "Ahmdanagar", "Dubai", "Australia"]
}

df = pd.DataFrame(studentData)
print(df)

df.to_csv("student_data.csv")