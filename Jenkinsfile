pipeline {
    agent any
    environment {
        IMG_NAME = 'job-portal'
        DOCKER_REPO = 'mohit3252/job-portal'
        K8S_DEPLOYMENT = 'job-portal'
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
                withCredentials([usernamePassword(credentialsId: 'DockerHub-LG', passwordVariable: 'PSWD', usernameVariable: 'LOGIN')]) {
                    script {

                        sh 'echo ${PSWD} | docker login -u ${LOGIN} --password-stdin'
                        sh 'docker push ${DOCKER_REPO}:${IMG_NAME}'
                    }

                }
            }
        }
            stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f k8s/deployment.yaml"
                sh "kubectl apply -f k8s/service.yaml"
            }
        }
    }
}
