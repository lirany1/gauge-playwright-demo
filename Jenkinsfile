pipeline {
    agent {
        docker {
            image 'python:3.13'
            args '-v $WORKSPACE:/app'
        }
    }
    
    environment {
        PYTHON_VERSION = '3.13'
        HOME = '/app'
    }
    
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    # Set working directory
                    cd /app
                    
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
                    # Install Node.js and npm
                    curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
                    apt-get install -y nodejs
                    
                    # Install Gauge and plugins
                    npm install -g @getgauge/cli
                    gauge install python
                    gauge install html-report
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    cd /app
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
