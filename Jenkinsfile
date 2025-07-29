pipeline {
    agent any

    environment {
        IMG_NAME = 'jobportal'
        DOCKER_REPO = 'mohit3252/job_portal'
        IMAGE_TAG = "${DOCKER_REPO}:${IMG_NAME}"
        TIMESTAMP = "${new Date().format('yyyyMMdd-HHmm', TimeZone.getTimeZone('IST'))}"
        KUBECONFIG = "${WORKSPACE}/kubeconfig"
        K8S_SERVER = 'https://192.168.49.2:8443'
    }
    
    triggers {
    pollSCM('H/5 * * * *')  // Every 5 minutes
    }
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def imageTag = "myapp:${env.TIMESTAMP}"
                    sh "docker build -t myrepo/${imageTag} ."
                    sh "docker push myrepo/${imageTag}"

            }
                    

        }
    }

    }
