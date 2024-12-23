from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Define the paths to LP Solve - make them environment-aware
def get_lpsolve_paths():
    # Check if we're in Streamlit Cloud
    if os.path.exists('/mount/src'):
        return {
            'include_dirs': ['/usr/include/lpsolve'],
            'library_dirs': ['/usr/lib/x86_64-linux-gnu'],
            'libraries': ['lpsolve55']
        }
    # Codespace paths
    return {
        'include_dirs': [r'/workspaces/deploy-streamlit-last/lpsolve'],
        'library_dirs': [r'/workspaces/deploy-streamlit-last/lpsolve'],
        'libraries': ['lpsolve55']
    }

paths = get_lpsolve_paths()

# Build the extension
extensions = [
    Extension(
        "clara.pylpsolve",
        ["clara/pylpsolve.pyx"],
        include_dirs=paths['include_dirs'],
        library_dirs=paths['library_dirs'],
        libraries=paths['libraries'],
    )
]

setup(
    ext_modules=cythonize(extensions, language_level="3"),
    package_data={
        'clara': ['liblpsolve55.so'],
      },
)