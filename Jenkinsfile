pipeline {
    agent any
    stages {
        
        stage('build') {
	    steps {
              sh 'echo "this"'
	      python setup.py
            }	

        }
        stage('Test') {
            steps {
              pip --version
              pip install coverage
              pip install pytest
	      pip install pytest-cov
              pip install python-coveralls
              py.test --cov-report= --cov=JenkinsDemoRepo tests.py

	     } 
        }

        stage('Deploy') {
            steps {


            }
       }
    }
}


