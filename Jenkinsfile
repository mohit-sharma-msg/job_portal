pipeline {
    agent any

    environment {
        IMAGE_NAME = 'mohit3252/job_portal'
        K8S_DEPLOYMENT = 'job_portal'
    }


        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f k8s/"
                sh "kubectl rollout restart deployment/${K8S_DEPLOYMENT}"
            }
        }
    }
}

