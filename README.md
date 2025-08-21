# Gauge-Playwright Demo

This project demonstrates automated testing using Gauge and Playwright in Python, with continuous integration using Jenkins on Kubernetes. It includes examples of web automation tests for navigating and interacting with web pages.

## Prerequisites

### Local Development
- Python 3.13
- Node.js and npm
- Gauge (`npm install -g @getgauge/cli`)
- Python packages (installed via pip):
  - getgauge
  - playwright

### CI/CD Requirements
- Kubernetes cluster (K3s)
- Jenkins installed on Kubernetes
- Jenkins plugins:
  - Pipeline
  - Git
  - HTML Publisher
  - Docker Pipeline

## Project Structure

```
├── specs/                  # Test specifications
│   ├── example.spec
│   └── jfrog_demo.spec
├── step_impl/             # Step implementations
│   ├── __init__.py
│   ├── jfrog_steps.py
│   └── step_impl.py
├── env/                   # Environment configurations
│   └── default/
├── start.sh              # Script to run tests
└── requirements.txt      # Python dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lirany1/gauge-playwright-demo.git
   cd gauge-playwright-demo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Running Tests

To run all specifications:
```bash
./start.sh run specs
```

To run a specific specification:
```bash
./start.sh run specs/jfrog_demo.spec
```

## Test Scenarios

The project includes test scenarios for:
- Navigating to JFrog website
- Interacting with web elements
- Taking screenshots
- Basic web automation tasks

## Reports

After test execution, HTML reports can be found in the `reports/html-report` directory.

## CI/CD Pipeline

This project includes a Jenkins pipeline for automated testing. The pipeline is defined in `Jenkinsfile` and includes the following stages:

1. **Debug Info**: Displays workspace and system information
2. **Checkout**: Clones the repository
3. **Setup Tools**: Installs Python 3.13 and required build tools
4. **Install Dependencies**: Sets up Python virtual environment and installs dependencies
5. **Install Gauge**: Installs Gauge and its plugins
6. **Run Tests**: Executes the test specifications
7. **Post Actions**: Publishes HTML reports and cleans up the workspace

### Setting up Jenkins Pipeline

1. Install Jenkins on Kubernetes:
   ```bash
   kubectl apply -f jenkins-k8s/
   ```

2. Install required Jenkins plugins:
   - Pipeline
   - Git
   - HTML Publisher
   - Docker Pipeline

3. Create a new Pipeline job in Jenkins:
   - Go to Jenkins dashboard
   - Click "New Item"
   - Select "Pipeline"
   - Configure:
     - Pipeline > Definition: "Pipeline script from SCM"
     - SCM: Git
     - Repository URL: `https://github.com/lirany1/gauge-playwright-demo.git`
     - Branch Specifier: `*/main`
     - Script Path: `Jenkinsfile`

### Running the Pipeline

1. Go to the pipeline job in Jenkins
2. Click "Build Now"
3. View test results in:
   - Console Output: Real-time test execution logs
   - Gauge Test Report: HTML report with detailed test results

### Troubleshooting

Common issues and solutions:
- **Permission Denied**: Ensure Jenkins pod has root permissions
- **Missing Tools**: The pipeline automatically installs required tools
- **Workspace Issues**: The pipeline includes cleanup steps

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

MIT License - feel free to use this demo project as a template for your own testing needs.
```
