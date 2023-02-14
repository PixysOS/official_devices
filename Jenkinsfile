pipeline {
    agent {
        label 'pixys'
    }

    environment {
        PASSWORD = credentials('OPENSSL_PASSWORD')
        SKIP_BUILD = sh script: "git log -1 | grep '[CI skip]'", returnStatus: true
        GIT_COMMIT_HASH = sh (script: "git log -n 1 --pretty=format:'%H'", returnStdout: true)
    }

    stages {
        stage("Skip build") {
            when {
                expression { "${SKIP_BUILD}" != "0" }
            }
            
            steps {
                script {
                    // Abort the build to avoid build loop
                    currentBuild.result = "ABORTED"
                }
            }
        }
        
        stage("Main") {
            steps {
                sh 'curl -L "https://raw.githubusercontent.com/PixysOS/official_devices/${GIT_COMMIT_HASH}/.github/scripts.tar.gz" --output scripts.tar.gz'
                sh 'openssl enc -d -aes256 -salt -pbkdf2 -in scripts.tar.gz -pass env:PASSWORD | tar xz'
                sh 'bash runner.sh'
            }
        }
    }
    
    post {
        cleanup {
            cleanWs()
        }
        success {
            sh 'python3 update_api.py SUCCESS'
        }
        failure {
            sh 'python3 update_api.py FAILURE'
        }
    }
}
