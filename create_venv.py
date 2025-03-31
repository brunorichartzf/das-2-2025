import os
import subprocess
import sys

def create_virtual_environment(venv_name=".venv", requirements_file="s3/requirements.txt"):
    # Step 1: Create the virtual environment
    print(f"Creating virtual environment '{venv_name}'...")
    subprocess.check_call([sys.executable, "-m", "venv", venv_name])
    print(f"Virtual environment '{venv_name}' created successfully.")

    # Step 2: Activate the virtual environment
    activate_script = os.path.join(venv_name, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_name, "bin", "activate")
    print(f"To activate the virtual environment, run: source {activate_script}" if os.name != "nt" else f"To activate the virtual environment, run: {activate_script}")

    # Step 3: Install dependencies from requirements.txt
    if os.path.exists(requirements_file):
        print(f"Installing dependencies from '{requirements_file}'...")
        subprocess.check_call([os.path.join(venv_name, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_name, "bin", "pip"), "install", "-r", requirements_file])
        print("Dependencies installed successfully.")
    else:
        print(f"Requirements file '{requirements_file}' not found. Skipping dependency installation.")

if __name__ == "__main__":
    create_virtual_environment()