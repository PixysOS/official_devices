/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent {
        node {
            label 'built-in'
        }
    }

    environment {
        PASSWORD = credentials('OPENSSL_PASSWORD')
        USER_CREDENTIALS = credentials('github')
        GIT_COMMIT_HASH = sh(script: "git log -n 1 --pretty=format:'%H'", returnStdout: true)
    }

    stages {
        stage('Main') {
            steps {
                script {
                    /* groovylint-disable-next-line GStringExpressionWithinString, LineLength */
                    sh 'curl -L "https://raw.githubusercontent.com/PixysOS/official_devices/${GIT_COMMIT_HASH}/.github/scripts.tar.gz" --output scripts.tar.gz'
                    sh 'openssl enc -d -aes256 -salt -pbkdf2 -in scripts.tar.gz -pass env:PASSWORD | tar xz'
                    sh 'bash runner.sh'
                }
            }
        }
    }

    post {
        cleanup {
            script {
                if (getContext(hudson.FilePath)) {
                    cleanWs()
                }
            }
        }
        success {
            script {
                if (getContext(hudson.FilePath)) {
                    sh 'python3 update_api.py SUCCESS'
                }
            }
        }
        failure {
            script {
                if (getContext(hudson.FilePath)) {
                    sh 'python3 update_api.py FAILURE'
                }
            }
        }
    }
}
