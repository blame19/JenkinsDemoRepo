pipeline {
    agent any
    stages {
        
        stage('build') {
	    steps {
              sh 'echo "this"'
              sh 'yum install python2-pip.noarch -y'
	      sh 'python setup.py'
            }	

        }
        stage('Test') {
            steps {
              
              sh 'pip 'install coverage'
              sh 'pip install pytest'
	      sh 'pip install pytest-cov'
              sh 'pip install python-coveralls'
              sh 'py.test --cov-report= --cov=JenkinsDemoRepo tests.py'

	     } 
        }

        stage('Deploy') {
            steps {
		sh 'echo "this"'
            }
       }
    }
}


