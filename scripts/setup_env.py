import os
import subprocess
import sys

def run_command(cmd, check=True):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=check)

def ensure_virtualenv():
    venv_path = os.path.join(os.getcwd(), ".venv", "Scripts" if os.name == 'nt' else "bin", "python.exe" if os.name == 'nt' else "python")
    if not os.path.exists(venv_path):
        print("❌ Virtual environment not found. Creating one...")
        run_command("python -m venv .venv")
        print("✅ Virtual environment created. Activating it...")
        activate_script = os.path.join(os.getcwd(), ".venv", "Scripts" if os.name == 'nt' else "bin", "activate")
        if os.name == 'nt':
            run_command(f"{activate_script} && python {__file__}")
        else:
            run_command(f"source {activate_script} && python {__file__}")
        sys.exit(0)

def main():
    ensure_virtualenv()

    # Ensure uv is available
    try:
        subprocess.run(["uv", "--version"], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("❌ 'uv' is not installed. Please install it from https://astral.sh/blog/uv/")
        sys.exit(1)

    # Install dependencies
    print("📦 Installing dependencies from pyproject.toml using uv...")
    run_command("uv pip install -r requirements.txt")

    # Install pre-commit if not already
    print("🔧 Installing pre-commit...")
    run_command("uv pip install pre-commit")

    # Run pre-commit install
    print("✅ Setting up pre-commit hook...")
    run_command("pre-commit install")   

    print("🚀 Project setup complete!")

if __name__ == "__main__":
    main()
