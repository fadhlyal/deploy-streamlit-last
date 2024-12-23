import subprocess
import os

try:
    # Update the path to match your setup
    base_path = "/workspaces/deploy-streamlit-last"
    
    os.environ['LD_LIBRARY_PATH'] = f"{base_path}/lpsolve:" + os.environ.get('LD_LIBRARY_PATH', '')

    print("Running setup.py to build extensions...")
    subprocess.check_call([
        "python", f"{base_path}/setup.py", "build_ext", "--inplace"
    ])
    print("Setup complete.")

    print("Checking shared object dependencies...")
    subprocess.check_call(["ldd", f"{base_path}/clara/pylpsolve.cpython-311-x86_64-linux-gnu.so"])

    print("Setting permissions for liblpsolve55.so...")
    subprocess.check_call(["chmod", "755", f"{base_path}/lpsolve/liblpsolve55.so"])

except subprocess.CalledProcessError as e:
    print(f"Error during setup: {e}")
