pipeline {

    agent any

    environment {
        registry = 'nvsailikhith/sentiment-analysis'
        DOCKERHUB_CREDS = credentials('DockerHubCred')
    }

    stages {

        stage('Stage 1: Git pull') {
            steps {
                git url: 'https://github.com/Likhith-2914/Sentiment-Analysis.git', branch: 'master'
            }
        }

        stage('Stage 2: Build') {
            steps {
                sh 'pip3 install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        // stage('Stage 3: Test') {
        //     steps {

        //     }
        // }

        stage('Stage 4: Docker image - frontend') {

            steps {
                
                script {
                    frontend_docker_image = docker.build("nvsailikhith/sentiment_analysis_frontend:latest", "./frontend")
                }
            }
        }

        stage('Stage 5: Docker image - backend') {
            steps {
                script {
                    backend_docker_image = docker.build("nvsailikhith/sentiment_analysis_frontend:latest", "./backend")
                }
            }
        }

        stage('Stage 6: Push docker images') {

            steps {

                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        frontend_docker_image.push()
                        backend_docker_image.push()
                    }
                }
            }
        }
    }
}