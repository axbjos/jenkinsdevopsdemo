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
    stage('deploy') {
      steps {
         sh 'ssh 192.168.56.105 touch /home/joeaxberg/testfile' 
      } 
    }
  }
}