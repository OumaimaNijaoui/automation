pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker_hub_oumaima')
    }


    stages {
        stage('build app'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'docker_hub_oumaima', url: 'https://github.com/OumaimaNijaoui/automation.git']]])
            }
        }
       

        stage('Docker Build') {
            steps {
               
                sh 'docker build -t oumaimanijaoui/devops:mytag .'
            }
        }
        stage('Push Image'){
            steps{
                script{
                    withCredentials([string(credentialsId: 'docker_hub_id', variable: 'docker_hub_pwd')]) {
                        sh 'docker logout'
                        sh 'docker network prune --force  '
                    sh ' docker login -u oumaimanijaoui -p ${docker_hub_pwd}'
                    
                   sh'docker push  oumaimanijaoui/devops:mytag '

}
                }
            }
        }
       
      
        }

    }