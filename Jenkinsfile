pipeline {
    agent any

    environment {
        AWS_REGION     = 'eu-north-1'
        AWS_ACCOUNT_ID = '179190112432'
        ECR_REPOSITORY = 'python-data-job'
        IMAGE_TAG      = "${env.BUILD_NUMBER}"  // ou "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $ECR_REPOSITORY:$IMAGE_TAG .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run --rm $ECR_REPOSITORY:$IMAGE_TAG pytest'
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                docker tag $ECR_REPOSITORY:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
                docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
                '''
            }
        }
    }
}
