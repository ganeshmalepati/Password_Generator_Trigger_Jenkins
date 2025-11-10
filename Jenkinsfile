pipeline {
    agent any
    
    environment {
        REPO_URL = 'https://github.com/ganeshmalepati/Password_Generator_Trigger_Jenkins.git'
        BRANCH = 'main'  // Change to 'master' if your repo uses that
    }

    stages {
        stage("Cloning Git Repository") {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage("Build Docker Image"){
            steps {
                sh 'docker build -t password-pipeline-job .'
            }
        }
        stage("Run Docker Container for python codes"){
            steps {
                sh 'docker run --rm password-pipeline-job'
            }
        }
    }

    post {
        always {
            echo "Pipeline has been successfully completed"
        }
    }
}
