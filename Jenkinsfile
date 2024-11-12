pipeline {
    agent {
        docker { image 'evansabraham/flask-sentiment-app' }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '/bin/bash -c "docker build -t ${DOCKER_IMAGE} ."'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '/bin/bash -c "python3 -m unittest test_app.py"'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '/bin/bash -c "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"'
                        sh '/bin/bash -c "docker push ${DOCKER_IMAGE}"'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '/bin/bash -c "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"'
                }
            }
        }
    }
}
