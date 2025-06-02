import os
import subprocess


def format_json(file_path):
    try:
        # Format using Prettier
        print(f"Formatting {file_path} with Prettier...")
        subprocess.run(["prettier", "--write", file_path], check=True)
        print(f"Formatted {file_path} with Prettier")
        # Add the formatted file to git staging
        subprocess.run(["git", "add", file_path], check=True)
    except Exception as e:
        print(f"Error formatting {file_path}: {e}")


def find_json_files():
    json_files = []
    for root, _, files in os.walk("."):  # Walk through current directory
        if "defs" in root:  # Check if 'defs' is in the folder path
            for file in files:
                if file.endswith(".json"):
                    json_files.append(os.path.join(root, file))
    return json_files


def main():
    json_files = find_json_files()
    for file_path in json_files:
        print(f"Processing {file_path}...")
        try:
            format_json(file_path)
        except Exception:
            print("Stopping due to formatting error.")
            return 1

    print("All files formatted successfully.")
    return 0


if __name__ == "__main__":
    result = main()
    exit(result)
