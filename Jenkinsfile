pipeline {
    agent any
    environment {
        IMG_NAME = 'jobportal'
        DOCKER_REPO = 'mohit3252/job_portal'
        IMAGE_TAG = "${IMG_NAME}:${TIMESTAMP}"
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
    stage('Configure Kubeconfig') {
            steps {
                // Inject the Kubernetes token stored as a Secret Text in Jenkins
                withCredentials([string(credentialsId: 'k8s-api-token', variable: 'K8S_TOKEN')]) {
                    sh '''
                        echo "Creating kubeconfig file..."

                        cat <<EOF > $KUBECONFIG
apiVersion: v1
kind: Config
clusters:
- name: kubernetes
  cluster:
    server: $K8S_SERVER
    insecure-skip-tls-verify: true
contexts:
- name: default-context
  context:
    cluster: kubernetes
    user: jenkins-user
current-context: default-context
users:
- name: jenkins-user
  user:
    token: $K8S_TOKEN
EOF

                        echo "Testing Kubernetes connection..."
                        kubectl get namespaces
                        kubectl get pods
                    '''
                }
            }
        }     
    }
    }
}
