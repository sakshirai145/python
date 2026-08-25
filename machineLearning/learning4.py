import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create Dataset
data = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rain", "Rain",
                "Rain", "Overcast", "Sunny", "Sunny", "Rain",
                "Sunny", "Overcast", "Overcast", "Rain"],

    "Temperature": ["Hot", "Hot", "Hot", "Mild", "Cool",
                    "Cool", "Cool", "Mild", "Cool", "Mild",
                    "Mild", "Mild", "Hot", "Mild"],

    "Humidity": ["High", "High", "High", "High", "Normal",
                 "Normal", "Normal", "High", "Normal", "Normal",
                 "Normal", "High", "Normal", "High"],

    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak",
             "Strong", "Strong", "Weak", "Weak", "Weak",
             "Strong", "Strong", "Weak", "Strong"],

    "Play": ["No", "No", "Yes", "Yes", "Yes",
             "No", "Yes", "No", "Yes", "Yes",
             "Yes", "Yes", "Yes", "No"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print(df)

# Encode categorical features
encoder = OrdinalEncoder()

df[["Outlook", "Temperature", "Humidity", "Wind"]] = encoder.fit_transform(
    df[["Outlook", "Temperature", "Humidity", "Wind"]]
)

# Encode target
df["Play"] = df["Play"].map({"No": 0, "Yes": 1})

print("\nEncoded Data")
print(df)

# X and Y
X = df.drop("Play", axis=1)
y = df["Play"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create SVM Model
model = SVC(kernel="linear")

# Train Model
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print("\nPrediction:")
print(prediction)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy:", accuracy)

# Predict New Data
new_data = [[2, 1, 0, 1]]

result = model.predict(new_data)

if result[0] == 1:
    print("\nPrediction for New Data: Yes")
else:
    print("\nPrediction for New Data: No")