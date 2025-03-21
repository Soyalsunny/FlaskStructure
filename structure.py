import os
from pathlib import Path
from flask_templates import templates  # Import the templates

class FlaskAppCreator:
    def __init__(self, base_path, app_name):
        self.base_path = Path(base_path) / app_name
        self.app_folder = app_name  # use app name inside structure too
        self.templates = templates
        self.app_name = app_name

    def create_structure(self):
        structure = {
            self.app_folder: {
                "__init__.py": f"{self.app_folder}/__init__.py",
                "models": {
                    "__init__.py": "",
                    "db.py": "models/db.py"
                },
                "routes": {
                    "__init__.py": "",
                    "abc.py": "routes/abc.py"
                },
                "schemas": {
                    "__init__.py": "",
                    "abcd.py": "schemas/abcd.py"
                },
                "utils": {
                    "__init__.py": "",
                    "abcde.py": "utils/abcde.py"
                },
                "tests": {
                    "__init__.py": "",
                    "test_app.py": "tests/test_app.py"
                },
                "config.py": "config.py",
                "main.py": "main.py"
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
                try:
                    with open(path, 'w') as file:
                        file_content = template.format(module_name=os.path.basename(os.path.dirname(path))) if template else ""
                        file.write(file_content)
                except OSError as e:
                    print(f"Error creating file {path}: {e}")

    def run(self):
        if self.base_path.exists():
            print(f"⚠️  Directory '{self.base_path}' already exists.")
        else:
            self.create_structure()
            print(f"✅ Flask app '{self.app_name}' created successfully at {self.base_path}.")

if __name__ == "__main__":
    user_input_path = input("📁 Enter the directory path where you want to create the Flask app: ").strip()
    app_name = input("📝 Enter the Flask app name: ").strip()
    
    creator = FlaskAppCreator(user_input_path, app_name)
    creator.run()
