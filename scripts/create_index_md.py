import os
import subprocess

# Function to create an index.md file and Markdown files for finding model definitions
def create_index_md():
    try:
        # Dynamically read Markdown files from the defs directory
        defs_dir = "./defs"
        finding_models = [os.path.join(defs_dir, f) for f in os.listdir(
            defs_dir) if f.endswith(".md")]

        # Create the index.md file with links to each model
        with open('index.md', 'w') as file:
            file.write('# Index\n\n')
            for model in finding_models:
                file.write(
                    f"- [{os.path.basename(model).capitalize()}](./{model})\n")
        print("index.md with model definition files created successfully.")
        try:
            subprocess.run(["git", "add", "index.md"], check=True)
            print("index.md file added to Git successfully.")
        except subprocess.CalledProcessError as git_error:
            print(f"Error adding index.md to Git: {git_error}")
        return 0
    except Exception as e:
        print(f"Error creating files: {e}")
        return 1


if __name__ == "__main__":
    exit(create_index_md())
