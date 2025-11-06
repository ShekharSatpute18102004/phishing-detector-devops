# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Train model at build time (optional, but safe)
RUN python -c "from phishing_detector import train_model; train_model()"

# Expose port
EXPOSE 8000

# Command to run your app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
