pipeline {
    agent any
    stages {
    	stage("Fix the permission issue") {


            steps {
                sh "sudo chown root:jenkins /run/docker.sock"
            }
         
        }
        stage('build') {
	    steps {
              sh 'python --version'
            }	

        }
    }
}


