pipeline {
  agent { none }
  stages {
    stage('build') {
      steps {
        sh 'ls -las'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py'
      }   
    }
  }
}