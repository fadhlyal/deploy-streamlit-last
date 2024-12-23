from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the paths to LP Solve
include_dirs = [r'/mount/src/deploy-streamlit-last/lpsolve']
library_dirs = [r'/mount/src/deploy-streamlit-last/lpsolve']
libraries = ["lpsolve55"]  # Replace with the correct library name if different

# Build the extension
extensions = [
    Extension(
        "clara.pylpsolve",
        ["clara/pylpsolve.pyx"],
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        libraries=libraries,
    )
]

setup(
    ext_modules=cythonize(extensions, language_level="3"),
)
