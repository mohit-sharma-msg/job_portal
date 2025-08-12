pipeline {
    agent any
    environment {
        IMAGE_NAME = "jobportal"
        IMAGE_TAG  = "2309-08122025"
        DOCKER_REPO = 'mohit3252/job_portal'
        IMAGE_TAG = "mohit3252/jobportal:${TIMESTAMP}"
        TIMESTAMP = "${new Date().format('HHmm-MMddyyyy', TimeZone.getTimeZone('IST'))}"
        KUBECONFIG = "${WORKSPACE}/kubeconfig"
        K8S_SERVER = 'https://192.168.49.2:8443'
        SONARQUBE = "MySonarQube"
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
                            sh '''echo "$PSWD" | docker login -u "$LOGIN" --password-stdin'''
                            sh "docker push ${IMAGE_TAG}"
                            sh "docker logout"
                        }
                    }
                }
             }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    withCredentials([string(credentialsId: 'sonar', variable: 'SONAR_TOKEN')]) {
                        sh """
                        sonar-scanner \
                          -Dsonar.projectKey=myapp \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=$SONAR_HOST_URL \
                          -Dsonar.login=$SONAR_TOKEN
                        """
                    }
                }
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh """
                trivy image --severity HIGH,CRITICAL --exit-code 1 --format table ${DOCKER_IMAGE}
                """
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
