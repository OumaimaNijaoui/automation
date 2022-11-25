pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker_hub_oumaima')
    }


    stages {
        stage('SCM Checkout') {
            steps {
                git 'https://github.com/OumaimaNijaoui/automation.git'
                
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t jenkinsImage:latest .'
            }
        }
        stage('Login to Dockerhub') {
          steps {
             sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin'
        }
      }
      stage('Push image'){

        steps{
            sh 'docker push jenkinsImage:latest'
        }
      }
        }

    }
        


