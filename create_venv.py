import os
import subprocess
import sys

def find_requirements_files():
    """Search for all 'requirements.txt' files in the current directory and subdirectories."""
    requirements_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file == "requirements.txt":
                requirements_files.append(os.path.join(root, file))
    return requirements_files

def choose_requirements_file(requirements_files):
    """Allow the user to choose a requirements file from the list."""
    if not requirements_files:
        print("No 'requirements.txt' files found.")
        return None

    print("Found the following 'requirements.txt' files:")
    for i, file in enumerate(requirements_files, start=1):
        print(f"{i}: {file}")

    while True:
        choice = input("Enter the number of the file you want to use (or press Enter to skip): ")
        if not choice:
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(requirements_files):
            return requirements_files[int(choice) - 1]
        print("Invalid choice. Please try again.")

def create_virtual_environment(venv_name=".venv"):
    # Step 1: Create the virtual environment
    print(f"Creating virtual environment '{venv_name}'...")
    subprocess.check_call([sys.executable, "-m", "venv", venv_name])
    print(f"Virtual environment '{venv_name}' created successfully.")

    # Step 2: Activate the virtual environment
    activate_script = os.path.join(venv_name, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_name, "bin", "activate")
    print(f"To activate the virtual environment, run: source {activate_script}" if os.name != "nt" else f"To activate the virtual environment, run: {activate_script}")

    # Step 3: Search for and choose a requirements file
    requirements_files = find_requirements_files()
    chosen_file = choose_requirements_file(requirements_files)

    # Step 4: Install dependencies from the chosen requirements file
    if chosen_file:
        print(f"Installing dependencies from '{chosen_file}'...")
        subprocess.check_call([os.path.join(venv_name, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_name, "bin", "pip"), "install", "-r", chosen_file])
        print("Dependencies installed successfully.")
    else:
        print("No requirements file selected. Skipping dependency installation.")

if __name__ == "__main__":
    create_virtual_environment()