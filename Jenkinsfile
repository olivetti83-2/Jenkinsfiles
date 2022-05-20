pipeline {
    agent {
        label('python')
    }
    stages {
        stage ('Test') {
            steps {
                sh 'echo Aloha!!!!!'
            }
        }
        stage ('Is there any python?'), (args:'-u root:root') {
            steps {
                sh 'python --version'
            }
        }
    }
}
