FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY phishing_detector.py .

# Skip model copy for now (uncomment when available)
COPY model.pkl vectorizer.pkl ./

EXPOSE 5000
CMD ["python", "app.py"]
