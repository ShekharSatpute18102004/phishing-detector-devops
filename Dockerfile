# =============================
# Phishing Detector - Dockerfile
# =============================

FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary project files
COPY app.py .
COPY phishing_detector.py .
COPY model.pkl vectorizer.pkl ./

# Expose Flask port
EXPOSE 8000

# Start Flask application
CMD ["python", "app.py"]
