pipeline {
  agent any

  environment {
    IMAGE_NAME = "yourdockerhubusername/phishing-detector"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install & Test') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements.txt pytest
          pytest -q
        '''
      }
    }

    stage('Docker Build') {
      steps {
        sh '''
          docker build -t $IMAGE_NAME:latest .
        '''
      }
    }

    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh '''
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker push $IMAGE_NAME:latest
          '''
        }
      }
    }
  }
}
