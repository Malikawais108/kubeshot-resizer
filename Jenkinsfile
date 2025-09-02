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
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
