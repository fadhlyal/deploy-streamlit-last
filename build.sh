#!/bin/bash
# Install system dependencies
apt-get update && apt-get install -y build-essential python3-dev liblpsolve55-dev

# Set LD_LIBRARY_PATH for lpsolve
if [ -d "/mount/src" ]; then
    # Streamlit Cloud environment
    export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
else
    # Codespace environment
    export LD_LIBRARY_PATH=/workspaces/deploy-streamlit-last/lpsolve:$LD_LIBRARY_PATH
fi

# Build the Cython extension
python setup.py build_ext --inplace