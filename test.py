import os

os.environ['LD_LIBRARY_PATH'] = '/workspaces/deploy-streamlit-last/lpsolve:' + os.environ.get('LD_LIBRARY_PATH', '')

print(os.environ['LD_LIBRARY_PATH'])