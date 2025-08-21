pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.13'
    }
    
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    # Install Python if not available
                    if ! command -v python3 &> /dev/null; then
                        apt-get update
                        apt-get install -y python3 python3-venv python3-pip
                    fi
                    
                    # Create and activate virtual environment
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    playwright install --with-deps
                '''
            }
        }
        
        stage('Install Gauge') {
            steps {
                sh '''
                    # Install Node.js and npm if not available
                    if ! command -v npm &> /dev/null; then
                        apt-get update
                        apt-get install -y nodejs npm
                    fi
                    
                    # Install Gauge and plugins
                    sudo npm install -g @getgauge/cli
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
