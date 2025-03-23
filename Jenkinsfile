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
                withCredentials([usernamePassword(credentialsId: 'DockerHub-LG', passwordVariable: '31dc75c356c34e8d82d227b86ec47ee4', usernameVariable: 'mohit3252
')]) {
                    script {
                        sh 'echo ${PSWD} | docker login -u ${LOGIN} --password-stdin'
                        sh 'docker push ${DOCKER_REPO}:${IMG_NAME}'
                    }
                }
            }
        }
    }
}
