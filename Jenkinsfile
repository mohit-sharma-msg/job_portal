pipeline {
    agent any
    environment {
        IMG_NAME = 'jobportal'
        DOCKER_REPO = 'mohit3252/job_portal'
        K8S_DEPLOYMENT = 'job_portal'
    }

            stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f k8s/"
                sh "kubectl rollout restart deployment/${K8S_DEPLOYMENT}"
            }
        }
    }
}
