# 🛡️ Phishing Website Detection Tool

## 📌 Problem Statement
Phishing websites are malicious sites designed to trick users into entering personal information such as login credentials, credit card numbers, or other sensitive data. This can lead to identity theft and financial fraud.

## 🎯 Objective
This project aims to build a lightweight detection tool that can identify potentially harmful URLs using either:
- Rule-based logic (with regex and string matching)
- Machine Learning techniques (with feature extraction and classification)

The goal is to help users detect suspicious links before interacting with them.

---
## 🧰 Requirements

### For Rule-Based Version
- Python 3.x
- `pandas`
- `re` (Regex)

### For Machine Learning Version
- `pandas`
- `scikit-learn`
- `numpy`

### Optional
- `tkinter` (for GUI version)

---

## 🧠 Features

- Detect phishing websites based on:
  - Rule-based logic: checks for red flags in URLs (e.g., IP addresses, hyphens, long URLs, suspicious keywords)
  - ML-based classification: trained model on labeled dataset (phishing vs. legitimate URLs)
- GUI (optional) for user-friendly interaction
- Lightweight and easy to deploy

---

## 🗂️ Project Structure

Project Structure
```
phishing-website-tool/
│
├── pycache/ # Cached Python files
│
├── static/ # Static frontend files
│ ├── script.js # JavaScript for frontend interaction
│ └── style.css # CSS for styling
│
├── templates/ # HTML templates
│ └── index.html # Frontend webpage
│
├── app.py # Flask web server entry point
├── phishing_detector.py # Core ML logic to detect phishing
├── model.pkl # Trained ML model
├── urls.csv # Dataset (URLs labeled as phishing or legitimate)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---

### 🔍 How It Works
- The user inputs a URL on the frontend.
- The backend uses a pre-trained ML model (model.pkl) and vectorizer (vectorizer.pkl) to analyze the URL features.
- The tool classifies the input as either:
   - ✅ Legitimate
   - ❌ Phishing

--- 

### 🚀 How to Run the Project
1. Clone the repository:
```
git clone https://github.com/your-username/phishing-website-tool.git
cd phishing-website-tool
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Start the Flask server:
```
python app.py
```
4. Access the tool:
Open your browser and navigate to http://127.0.0.1:5000/


## 📄 License
MIT License - feel free to use and adapt!
