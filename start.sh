#!/bin/bash

# Set the Python interpreter path
VENV_PYTHON="/Users/liran/gauge-demo/gauge-playwright-demo/.venv/bin/python"

# Check if the virtual environment Python exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "Error: Python interpreter not found at $VENV_PYTHON"
    exit 1
fi

# Export the Python path for Gauge
export GAUGE_PYTHON_COMMAND="$VENV_PYTHON"

# Run Gauge with all arguments passed to this script
exec gauge "$@"
