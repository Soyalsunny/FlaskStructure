import os
from pathlib import Path
from flask_templates import templates  # Import the templates

class FlaskAppCreator:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.templates = templates

    def create_structure(self):
        structure = {
            "app": {
                "__init__.py": "app/__init__.py",
                "models": {
                    "__init__.py": "",
                    "db.py": ""
                },
                "routes": {
                    "__init__.py": "",
                    "abc.py": ""
                },
                "schemas": {
                    "__init__.py": "",
                    "abcd.py": ""
                },
                "utils": {
                    "__init__.py": "",
                    "abcde.py": ""
                },
                "config.py": "",
                "main.py": ""
            }
        }
        self._create_files(self.base_path, structure)

    def _create_files(self, base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                self._create_files(path, content)
            else:
                template_key = content if content else name
                template = self.templates.get(template_key, "# Default content\n")
                with open(path, 'w') as file:
                    file_content = template.format(module_name=os.path.basename(os.path.dirname(path))) if template else ""
                    file.write(file_content)

    def run(self):
        if not self.base_path.exists() or not self.base_path.is_dir():
            print("Error: The specified path does not exist or is not a directory.")
            return
        self.create_structure()
        print(f"Flask app directory structure created successfully at {self.base_path}.")

if __name__ == "__main__":
    user_input = input("Enter the directory path where you want to create the Flask app structure: ")
    creator = FlaskAppCreator(user_input)
    creator.run()
