pipeline {
    agent {
        label 'python3'
    }
    stages {
        stage ('Test') {
            steps {
                sh 'echo Aloha!!!!!'
            }
        }
        stage ('Is there any python?') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}
