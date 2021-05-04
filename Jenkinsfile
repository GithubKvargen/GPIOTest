pipeline {
    agent any 
    stages {
        stage('Static Analysis') {
            steps {
                echo 'Run the static analysis to the code' 
            }
        }
        stage('Compile') {
            steps {
                echo 'Compile the source code' 
            }
        }
        stage('Security Check') {
            steps {
                echo 'Run the security check against the application' 
                sh "git config --global user.email jeffes159@gmail.com"
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh "python --version"
                sh "whoami"
                sh "ls"

                dir("${WORKSPACE}/GPIOtest/PedalApplication/Pedal/"){
                    sh "python -m robot PedalApp.robot"
                }
                
            }
        }
        stage('Run Integration Tests') {
            steps {
                echo 'Run only crucial integration tests from the source code' 
            }
        }
        stage('Publish Artifacts') {
            steps {
                echo 'Save the assemblies generated from the compilation' 
            }
        }
    }
}
