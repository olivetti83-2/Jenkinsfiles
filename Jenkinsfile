pipeline {
    agent {
        label('python')
    }
    stages {
        stage('Test') {
            steps {
                sh 'echo Aloha!!!!!'
            }
        }
        stage('Is there any python?') {
            steps {
                sh 'python --version'
            }
        }
    }
}