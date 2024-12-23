import os

# os.environ['LD_LIBRARY_PATH'] = '/mount/src/deploy-streamlit-last/lpsolve:' + os.environ.get('LD_LIBRARY_PATH', '')
# os.environ['PYTHONPATH'] = '/mount/src/deploy-streamlit-last:' + os.environ.get('PYTHONPATH', '')

print(f"LD_LIBRARY_PATH: {os.environ.get('LD_LIBRARY_PATH')}")
print(f"PYTHONPATH: {os.environ.get('PYTHONPATH')}")