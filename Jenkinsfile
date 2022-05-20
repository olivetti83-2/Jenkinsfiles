pipeline {
    agent {
        docker{
            label 'python'
            image 'oliverp83/python-jenkins-agent'
        }
        
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
