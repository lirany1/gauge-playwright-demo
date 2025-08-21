pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.13'
    }
    
    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }
        
        stage('Install Gauge') {
            steps {
                sh '''
                    npm install -g @getgauge/cli
                    gauge install python
                    gauge install html-report
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    chmod +x start.sh
                    ./start.sh run specs/
                '''
            }
        }
    }
    
    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports/html-report',
                reportFiles: 'index.html',
                reportName: 'Gauge Test Report',
                reportTitles: ''
            ])
            
            cleanWs()
        }
    }
}
