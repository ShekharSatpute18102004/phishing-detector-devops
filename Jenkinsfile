pipeline {
    agent any

    environment {
        IMAGE_NAME = "phishing-detector"
        CONTAINER_NAME = "phishing-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ShekharSatpute18102004/phishing-detector-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🛠 Building Docker image..."
                    sh 'docker run -d -p 8000:8000 --name phishing-container ${IMAGE_NAME}:latest'

                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "🚀 Running Docker container..."
                    // Stop existing container if any
                    sh 'docker ps -q --filter "name=${CONTAINER_NAME}" | grep -q . && docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME} || true'
                   // Start new container on port 5000
                    sh 'docker run -d -p 5000:5000 --name phishing-container ${IMAGE_NAME}:latest'

                }
            }
        }

        stage('Post Build') {
            steps {
                echo "✅ Deployment Successful! Access app at http://localhost:5000"
            }
        }
    }

    post {
        failure {
            echo "❌ Build failed. Check the console output for errors."
        }
    }
}
