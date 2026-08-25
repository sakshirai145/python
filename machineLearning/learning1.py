import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Create Dictionary
data = {
    "Hours_Studied": [1, 2, None, 4, 5, None, 7, 8],
    "Marks": [35, 45, 50, 65, 75, 80, 90, 95],
    "Result": ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass"]
}

# Convert Dictionary to DataFrame
df = pd.DataFrame(data)

print("Original Data")
print(df)

# Remove rows having missing values
df = df.dropna()

print("\nData After Removing Missing Values")
print(df)

# Store X and Y
X = df["Hours_Studied"]
Y = df["Marks"]

# Draw Line Graph
plt.figure(figsize=(6,4))
plt.plot(X, Y, marker='o')

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

plt.show()

