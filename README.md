# Gauge-Playwright Demo

This project demonstrates automated testing using Gauge and Playwright in Python. It includes examples of web automation tests for navigating and interacting with web pages.

## Prerequisites

- Python 3.x
- Gauge (`npm install -g @getgauge/cli`)
- Python packages (installed via pip):
  - getgauge
  - playwright

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
