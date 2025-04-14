import os
import subprocess
import platform

# Function to create a virtual environment
def create_virtual_environment():
    try:
        subprocess.check_call(['python', '-m', 'venv', 'env'])
        print("Virtual environment created successfully.")
    except Exception as e:
        print(f"Error creating virtual environment: {e}")
        raise

# Function to install dependencies
def install_dependencies():
    try:
        pip_executable = 'env\\Scripts\\pip' if platform.system() == 'Windows' else 'env/bin/pip'
        subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        raise

# Function to set up pre-commit hooks
def setup_pre_commit_hooks():
    try:
        pip_executable = 'env\\Scripts\\pip' if platform.system() == 'Windows' else 'env/bin/pip'
        subprocess.check_call([pip_executable, 'install', 'pre-commit'])
        # Check if core.hooksPath is set before unsetting it
        try:
            subprocess.check_call(['git', 'config', '--get', 'core.hooksPath'])
            subprocess.check_call(['git', 'config', '--unset-all', 'core.hooksPath'])
        except subprocess.CalledProcessError:
            # core.hooksPath is not set, no need to unset
            pass
        subprocess.check_call(['env\\Scripts\\pre-commit' if platform.system() == 'Windows' else 'env/bin/pre-commit', 'install'])
        print("Pre-commit hooks installed successfully.")
    except Exception as e:
        print(f"Error setting up pre-commit hooks: {e}")
        raise

if __name__ == "__main__":
    create_virtual_environment()
    install_dependencies()
    setup_pre_commit_hooks()