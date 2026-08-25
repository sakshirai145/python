from sklearn.preprocessing import StandardScaler

from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

import pandas as pd

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

df = pd.DataFrame(data)

print(df)

encoder = OrdinalEncoder()

df[["Outlook","Temperature","Humidity","Wind"]] = encoder.fit_transform(
    df[["Outlook","Temperature","Humidity","Wind"]]
)

df["Play"] = df["Play"].map({"No":0,"Yes":1})

print(df)

X = df.drop("Play", axis=1)

y = df["Play"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = CategoricalNB()
model.fit(X_train, y_train)