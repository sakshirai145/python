from numpy import int64
import pandas as pd

# Creating a DataFrame
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Aman", "Priya", "Rahul", "Sneha", "Karan", "Neha"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Course": ["CSE", "IT", "ECE", "CSE", "ME", "IT"],
    "Marks": [85, 92, None, 88, None, 95],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)


print(df["Marks"].mean())

print(df["Marks"].median())


print(df.isnull().sum())
print(df.info())

print(df["Marks"].isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)

df = pd.get_dummies(df["Gender"], prefix="Gender").astype(int64)
print(df)



