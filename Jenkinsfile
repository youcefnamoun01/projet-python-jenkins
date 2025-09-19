pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-3'
        ECR_REPOSITORY = 'python-data-job-2'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
        steps {
            sh '''
            apt-get update
            apt-get install -y python3 python3-pip
            pip3 install -r requirements.txt
            '''
        }
        }

        stage('Run Tests') {
            steps {
                sh 'export PYTHONPATH=$PYTHONPATH:$(pwd) && pytest'
            }
        }

        /*stage('Build Docker Image') {
            steps {
                sh 'docker build -t $ECR_REPOSITORY:$IMAGE_TAG .'
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.$AWS_REGION.amazonaws.com
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                docker tag $ECR_REPOSITORY:$IMAGE_TAG <AWS_ACCOUNT_ID>.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
                docker push <AWS_ACCOUNT_ID>.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
                '''
            }
        }*/
    }
}
