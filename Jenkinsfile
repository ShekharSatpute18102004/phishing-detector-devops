pipeline {
    agent any

    environment {
        IMAGE_NAME = "phishing-detector"
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
                    dockerImage = docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop & remove any old running container
                    sh 'docker ps -q --filter "name=phishing-container" | grep -q . && docker stop phishing-container && docker rm phishing-container || true'

                    // Run new container
                    sh 'docker run -d -p 5000:5000 --name phishing-container ${IMAGE_NAME}:latest'
                }
            }
        }

        stage('Post Build') {
            steps {
                echo "✅ Build completed successfully! App running on http://localhost:5000"
            }
        }
    }
}
