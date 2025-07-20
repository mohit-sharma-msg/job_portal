pipeline {
    agent any

    environment {
        IMG_NAME = 'jobportal'
        DOCKER_REPO = 'mohit3252/job_portal'
        IMAGE_TAG = "${DOCKER_REPO}:${IMG_NAME}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "export HOME=/var/lib/jenkins && docker build -t ${IMG_NAME} ."
                    sh "docker tag ${IMG_NAME} ${IMAGE_TAG}"
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub-LG', passwordVariable: 'PSWD', usernameVariable: 'LOGIN')]) {
                    script {
                        sh "echo ${PSWD} | docker login -u ${LOGIN} --password-stdin"
                        sh "docker push ${IMAGE_TAG}"
                        sh "docker logout"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'k8s-cluster-config', variable: 'KUBECONFIG_FILE')]) {
                    script {
                        sh '''
                            export KUBECONFIG=${KUBECONFIG_FILE}
                            kubectl set image deployment/jobportal-deployment jobportal-container=${IMAGE_TAG} --namespace=default
                        '''
                    }
                }
            }
        }
    }
}
