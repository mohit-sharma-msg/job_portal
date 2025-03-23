pipeline {
    agent any
    environment {
        IMG_NAME = 'jobportal'
        DOCKER_REPO = 'mohit3252/job_portal'
    }
    stages {
        stage('build') {
            steps {
                script {
                        sh 'export HOME=/var/lib/jenkins && docker build -t ${IMG_NAME} .'       
                        sh 'docker tag ${IMG_NAME} ${DOCKER_REPO}:${IMG_NAME}'
                }
            }
        }
        stage('push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub-LG', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
    // Log in to DockerHub using the credentials
    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASSWORD'
}


                }
            }
        }
    }
}
