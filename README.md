## 🛡️ Phishing Website Detection Tool (Flask + ML + DevOps)
## 📖 Overview

This project is a Phishing Website Detection Tool built using Flask, Machine Learning (Random Forest), and Rule-Based Detection. It provides a simple web interface to check whether a URL is legitimate or phishing based on predefined rules and a trained model. The project is fully containerized using Docker and automated with Jenkins in a CI/CD pipeline.

## 🚀 Features

🔍 Detects phishing URLs using rule-based logic and ML.

🧠 Machine Learning Model (Random Forest) trained on sample dataset.

🌐 Flask Web App for user-friendly interaction.

🐳 Dockerized for consistent environment and easy deployment.

⚙️ Jenkins Pipeline for automated testing, building, and deployment.

## 🧱 Tech Stack
```
Component	            Technology
Frontend	            HTML, CSS (Flask Templates)
Backend	              Flask (Python)
Machine Learning	    scikit-learn, pandas, joblib
Server	              Gunicorn (WSGI)
Containerization	    Docker
CI/CD	                Jenkins + DockerHub + GitHub
```

## 🗂️ Project Structure

Project Structure
```
phishing-detector/
├── app.py
├── phishing_detector.py
├── urls.csv
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .dockerignore
├── .gitignore
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── tests/
└── test_smoke.py
```
## 🧠 How It Works

- Rule-Based Detection: Uses basic URL pattern checks (e.g., missing HTTPS, presence of @, long URLs, IPs).
- ML-Based Detection: Uses a pre-trained Random Forest model on tokenized URLs.
- Integration: Combines both approaches to display results in an intuitive web interface.

## 🧩 Installation (Local)
1️⃣ Clone the Repository
```
git clone https://github.com/ShekharSatpute18102004/phishing-detector-devops.git
cd phishing-detector
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Run the App
```
python app.py
```
Visit: http://127.0.0.1:5000

## 🐳 Docker Setup
Build Docker Image
```
docker build -t phishing-detector .
```
Run Container
```
docker run -d -p 8000:8000 phishing-detector
```
Visit: http://localhost:8000

## ⚙️ Jenkins CI/CD Pipeline
Jenkinsfile Pipeline Stages:
1. Checkout – Pull code from GitHub.
2. Install & Test – Set up Python, install dependencies, and run pytest.
3. Docker Build – Build Docker image.
4. Docker Push – Push image to DockerHub.

## Jenkins Setup:

1. Run Jenkins inside Docker:
```
 docker run -d \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```
2. Install suggested plugins + Docker plugin.
3. Add DockerHub credentials (ID: dockerhub-creds).
4. Create a Pipeline Job → use SCM → link to your GitHub repo.
5. Run the build to automate the full CI/CD process.

## 📄 License
MIT License - feel free to use and adapt!
