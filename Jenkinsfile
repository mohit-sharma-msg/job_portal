pipeline {
    agent any

    environment {
        IMG_NAME = 'jobportal'
        
        TIMESTAMP = "" // Will be set dynamically
        
        DOCKER_REPO = 'mohit3252/job_portal'
        IMAGE_TAG = "${DOCKER_REPO}:${IMG_NAME}"
        KUBECONFIG = "${WORKSPACE}/kubeconfig" 
        K8S_SERVER = 'https://192.168.49.2:8443'
    }
        triggers {
        pollSCM('H/5 * * * *') 
    }
    stages {
                stage('Checkout') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/mohit-sharma-msg/job_portal.git'
            }
        }
        stage('Prepare Timestamp Tag') {
            steps {
                script {
                    def ts = new Date().format("yyyy-MM-dd-HH-mm", TimeZone.getTimeZone('Asia/Kolkata'))
                    env.IMAGE_TAG = "${DOCKER_IMAGE}:${ts}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        export HOME=/var/lib/jenkins
                        docker build -t ${IMG_NAME} .
                        docker tag ${IMG_NAME} ${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub-LG', passwordVariable: 'PSWD', usernameVariable: 'LOGIN')]) {
                    script {
                        sh '''
                            echo "$PSWD" | docker login -u "$LOGIN" --password-stdin
                            docker push ${IMAGE_TAG}
                            docker logout
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Image pushed: ${IMAGE_TAG}"
        }
        failure {
            echo "❌ Failed to push Docker image."
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
                    '''
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo 'Deploying to Kubernetes...'
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                }
            }
        }
                    
        stage('Verify Deployment') {
            steps {
                script {
                    sh 'kubectl get pods'
                    sh 'kubectl get svc'
                }
            }
        }
        
    }

    }

