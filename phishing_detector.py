import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# ---------- Rule-Based Detection ----------
def is_phishing_url_rule(url, return_reason=False):
    # Your rule logic
    if "http://" in url and return_reason:
        return True, "No HTTPS"
    elif "@" in url and return_reason:
        return True, "Suspicious '@' character"
    # ...
    return False, "Safe" if return_reason else False


# ---------- ML-Based Detection ----------
def train_model():
    df = pd.read_csv("urls.csv")

    # Drop rows with missing labels
    df.dropna(subset=['Label'], inplace=True)

    # Map labels to numeric
    df['Label'] = df['Label'].map({'legitimate': 0, 'phishing': 1})

    # Drop rows with unmapped (NaN) labels
    df.dropna(subset=['Label'], inplace=True)

    # Vectorize URLs
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['URL'])
    y = df['Label']

    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Save model
    import joblib
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    
def is_phishing_url_ml(url):
    import joblib
    vectorizer = joblib.load('vectorizer.pkl')
    model = joblib.load('model.pkl')

    # Transform the URL
    X = vectorizer.transform([url])

    # Predict
    prediction = model.predict(X)

    return prediction[0] == 1  # Return True if phishing, False if legitimate