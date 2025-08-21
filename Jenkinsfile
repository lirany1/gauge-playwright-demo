pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.13'
    }
    
    stages {
        stage('Setup Tools') {
            steps {
                sh '''
                    # Download and install Python
                    wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz
                    tar xzf Python-3.13.0.tgz
                    cd Python-3.13.0
                    ./configure --enable-optimizations
                    make altinstall
                    cd ..
                    rm -rf Python-3.13.0 Python-3.13.0.tgz
                    
                    # Install Node.js
                    curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
                    bash nodesource_setup.sh
                    apt-get install -y nodejs
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    # Create and activate virtual environment
                    python3.13 -m venv .venv
                    . .venv/bin/activate
                    
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
            node('any') {
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
}
