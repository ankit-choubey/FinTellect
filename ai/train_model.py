import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample training data (Ideally, replace this with real user data)
data = {
    "description": [
        "Groceries from supermarket", "Netflix subscription", "Invested in stocks",
        "Electricity bill", "Bought new shoes", "Mutual fund investment",
        "Salary credited", "Dining at a restaurant", "Monthly rent"
    ],
    "category": [
        "Essentials", "Wants", "Investments", "Essentials", "Wants",
        "Investments", "Savings", "Wants", "Essentials"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert text descriptions into numerical data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["description"])
y = df["category"]

# Train a classification model
model = RandomForestClassifier()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, "ai/spending_model.pkl")
joblib.dump(vectorizer, "ai/vectorizer.pkl")

print("✅ AI Model Trained and Saved!")
