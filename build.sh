#!/bin/bash
# Install system dependencies
apt-get update && apt-get install -y build-essential python3-dev liblpsolve55-dev

# Build the Cython extension
python setup.py build_ext --inplace