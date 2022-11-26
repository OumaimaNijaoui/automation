node {
     environment {
        DOCKERHUB_CREDENTIALS = credentials('docker_hub_oumaima')
    }

    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("getintodevops/hellonode")
    }



    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}



// pipeline {
//     agent any
//     environment {
//         DOCKERHUB_CREDENTIALS = credentials('docker_hub_oumaima')
//     }


//     stages {
//         stage('build app'){
//             steps{
//                 checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'docker_hub_oumaima', url: 'https://github.com/OumaimaNijaoui/automation.git']]])
//             }
//         }
       

//         stage('Docker Build') {
//             steps {
               
//                 sh 'docker build -t oumaimanijaoui/devops:mytag .'
//             }
//         }
//         stage('Push Image'){
//             steps{
//                 script{
//                     withCredentials([string(credentialsId: 'docker_hub_id', variable: 'docker_hub_pwd')]) {
//                         sh 'docker logout'
                       
//                     sh ' docker login -u oumaimanijaoui -p ${docker_hub_pwd}'
                    
//                    sh'docker push  oumaimanijaoui/devops:mytag '

// }
//                 }
//             }
//         }
       
      
//         }

//     }