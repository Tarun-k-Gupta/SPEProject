pipeline {

    agent any

    environment {
        registry = 'nvsailikhith/sentiment-analysis'
        DOCKERHUB_CREDS = credentials('DockerHubCred')
        dockerimage = ''
    }

    stages {

        stage('Git pull') {
            steps {
                git url: 'https://github.com/Likhith-2914/Sentiment-Analysis.git', branch: 'master'
            }
        }

        stage('Build') {
            steps {
                sh 'pip3 install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh '''cd backend
                    python3 download_models.py'''
            }
        }
    }
}