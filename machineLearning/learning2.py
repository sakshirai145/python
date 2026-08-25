import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
# Dataset
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

# DataFrame
df = pd.DataFrame(data)

print(df)

# Encode categorical columns
encoder = OrdinalEncoder()

df[["Outlook", "Temperature", "Humidity", "Wind"]] = encoder.fit_transform(
    df[["Outlook", "Temperature", "Humidity", "Wind"]]
)

# Encode target column
df["Play"] = df["Play"].map({"No": 0, "Yes": 1})

print(df)

# X and Y
X = df.drop("Play", axis=1)
y = df["Play"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = CategoricalNB()

# Train
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

print("Prediction:")
print(prediction)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)
cm = confusion_matrix(y_test, prediction)
print("Confusion Matrix:")
print(cm)
print("Classification Report:")
print(classification_report(y_test, prediction))
