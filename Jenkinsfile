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
                sh 'pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu'
            }
        }

        stage('Stage 3: Test') {
            steps {

                sh '''cd tester
                    python3 tester.py'''

            }
        }

        stage('Stage 4: Docker image - frontend') {

            steps {
                
                script {
                    frontend_docker_image = docker.build("nvsailikhith/sentiment_analyzer_frontend:latest", "./frontend")
                }
            }
        }

        stage('Stage 5: Docker image - backend') {
            steps {
                script {
                    backend_docker_image = docker.build("nvsailikhith/sentiment_analyzer_backend:latest", "./backend")
                }
            }
        }

        stage('Stage 6: Push frontend docker image') {

            steps {

                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        frontend_docker_image.push()
                    }
                }
            }
        }

        stage('Stage 7: Push backend docker image') {

            steps {

                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        backend_docker_image.push()
                    }
                }
            }
        }

        stage('Stage 8: Clear Cache') {
            steps {

                sh 'docker container prune -f'
                sh 'docker image prune -f'
            }
        }

        stage('Stage 9: Ansible Deploy') {
            steps {
                ansiblePlaybook becomeUser: null,
                colorized: true,
                credentialsId: 'localhost',
                disableHostKeyChecking: true,
                installation: 'Ansible',
                inventory: 'inventory',
                playbook: 'ansible-playbook.yml',
                sudoUser: null

                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                sh 'docker-compose down' //Stopping and removing the containers and networks linked to the project
            }
        }
    }
}
