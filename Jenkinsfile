pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'evansabraham/flask-sentiment-app'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Load .env file') {
            steps {
                script {
                    // Load .env file into the environment
                    // On Mac or Linux, you can source it using 'sh' command
                    sh 'export $(cat .env | xargs)'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image using the environment variables
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Run Python tests
                    sh 'python3 -m unittest test_app.py'
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub with credentials from .env file
                    sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                    
                    // Push Docker image to Docker Hub
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Deploy the Docker container
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }
}
