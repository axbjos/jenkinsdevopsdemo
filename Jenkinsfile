pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'ls -las'
      }
    }
    stage('test') {
      steps {
        sh '/Users/joeaxberg/Documents/Jenkins/microblog/venv/bin/python3 test.py'
      }   
    }
  }
}