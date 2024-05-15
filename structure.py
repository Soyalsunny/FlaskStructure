import os
from pathlib import Path

def create_structure(base_path, structure):
    """ Recursively creates directories and files based on the `structure` dictionary. """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            
            with open(path, 'w') as file:
                file.write(content)

def main():
    # Ask user for  location
    user_input = input("Enter the directory path where you want to create the Flask app structure: ")
    base_path = Path(user_input)

    # Check if the path exists and is a directory
    if not base_path.exists() or not base_path.is_dir():
        print("Error: The specified path does not exist or is not a directory.")
        return

    
    structure = {
        "app": {
            "__init__.py": "",
            "models": {
                "__init__.py": "",
                "db.py": "# Contains database models"
            },
            "routes": {
                "__init__.py": "",
                "abc.py": "# Route definitions"
            },
            "schemas": {
                "__init__.py": "",
                "abcd.py": "# Marshmallow schemas for serialization"
            },
            "utils": {
                "__init__.py": "",
                "abcde.py": "# Utility functions"
            }
        },
        "config.py": "# Contains configuration settings",
        "main.py": "# The main entry point for starting the Flask app"
    }

    
    create_structure(base_path, structure)

    print(f"Flask app directory structure created successfully at {base_path}.")

if __name__ == "__main__":
    main()