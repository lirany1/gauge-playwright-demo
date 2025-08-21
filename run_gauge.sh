#!/bin/bash
export PATH="/Users/liran/gauge-demo/.venv/bin:$PATH"
export PYTHONPATH="/Users/liran/gauge-demo/gauge-playwright-demo/step_impl:$PYTHONPATH"
gauge "$@"
