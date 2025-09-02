pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'MySonarQubeServer'   // Must match the name in Jenkins → Configure System → SonarQube Servers
        SONAR_TOKEN = credentials('SONAR_TOKEN') // Jenkins credential ID for your SonarQube token
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Malikawais108/extra.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh "/opt/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner -Dsonar.login=$SONAR_TOKEN"
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully and passed the quality gate."
        }
        failure {
            echo "❌ Pipeline failed. Check logs for details."
        }
    }
}
