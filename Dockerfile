# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
