import os

# Function to create an index.md file
def create_index_md():
    try:
        with open('index.md', 'w') as file:
            file.write('# Index\n\nThis is the index file.')
        print("index.md file created successfully.")
    except Exception as e:
        print(f"Error creating index.md file: {e}")
        raise

if __name__ == "__main__":
    create_index_md()