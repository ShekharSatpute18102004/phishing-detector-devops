from flask import Flask, render_template, request
import joblib
from phishing_detector import is_phishing_url_rule, train_model
from sklearn.feature_extraction.text import CountVectorizer
import os

app = Flask(__name__)

# Load model and vectorizer
if not os.path.exists("model.pkl"):
    train_model()

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        suspicious, reason = is_phishing_url_rule(url, return_reason=True)
        rule_result = "Suspicious" if suspicious else "Legitimate"

        X = vectorizer.transform([url])
        proba = model.predict_proba(X)[0][1]
        ml_confidence = f"{round(proba * 100)}% phishing confidence"

        result = {
            "url": url,
            "rule": rule_result,
            "rule_reason": reason,
            "ml": ml_confidence
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

