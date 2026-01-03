pipeline {
    agent any

    environment {
        AWS_REGION = "eu-north-1"
        ECR_REPO = "836622696787.dkr.ecr.eu-north-1.amazonaws.com/docker_project-coffee-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Gnanendra-sairam/devops-project.git'
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-ecr-creds'
                ]]) {
                    sh '''
                    aws ecr get-login-password --region $AWS_REGION \
                    | docker login --username AWS --password-stdin $ECR_REPO
                    '''
                }
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t coffee-app .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag coffee-app:latest $ECR_REPO:latest'
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh 'docker push $ECR_REPO:latest'
            }
        }
    }
}
