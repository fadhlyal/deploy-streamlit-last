#!/bin/bash
# Install system dependencies
apt-get update && apt-get install -y build-essential python3-dev liblpsolve55-dev

# Copy lpsolve files to the correct location in Streamlit Cloud
mkdir -p /mount/src/deploy-streamlit-last/lpsolve
cp -r lpsolve/* /mount/src/deploy-streamlit-last/lpsolve/

# Set LD_LIBRARY_PATH exactly as in Codespaces
export LD_LIBRARY_PATH=/mount/src/deploy-streamlit-last/lpsolve

# Build the Cython extension
python setup.py build_ext --inplace

# Add the library path to system-wide configuration
echo "/mount/src/deploy-streamlit-last/lpsolve" > /etc/ld.so.conf.d/lpsolve.conf
ldconfig