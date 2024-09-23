# Flask Application Structure

This repository contains a basic Flask application structured for scalability and maintainability. The project is organized to support large-scale applications through a modular design.

## Installation
You can install **FlaskFolderStructure** using pip:

```bash
pip install FlaskFolderStructure

```

## Motivation

The motivation behind creating FlaskFolderStructure was to provide a quick and standardized way to scaffold a Flask application with all the necessary folders and files in place, helping developers focus on the core logic of their applications rather than spending time organizing the project structure.

## Features

Generates a well-structured Flask application folder system.
Supports creating basic components like models, routes, schemas, utilities, and tests.
Customizable template-based folder creation.
Easily integrates into any new or existing Flask project.

## Project Structure

Below is the project directory structure along with a brief description of each component:
```
/flask_app
│
├── app/
│ ├── init.py # Initializes the app as a package and includes any application configurations
│ ├── models/
│ │ ├── init.py # Makes models a Python package
│ │ └── db.py # Contains database models
│ ├── routes/
│ │ ├── init.py # Makes routes a Python package
│ │ └── abc.py # Route definitions
│ ├── schemas/
│ │ ├── init.py # Makes schemas a Python package
│ │ └── abcd.py # Marshmallow schemas for serializing and deserializing data
│ └── utils/
│ ├── init.py # Makes utils a Python package
│ └── abcde.py # Utility functions
│
├── config.py # Contains configuration settings
└── main.py # The main entry point for starting the Flask app
```
## API

### create_structure(base_path)

This is the main method responsible for creating the folder structure at the specified base_path. It uses the default or custom templates to create the necessary files and directories.

## Template Customization

You can customize any part of the generated folder structure by providing your own templates via the templates argument when initializing FlaskAppCreator.

```python
from flask_folder_structure import FlaskAppCreator

custom_templates = {
    "config.py": "# Custom config settings",
    "main.py": "# Custom main.py content"
}

creator = FlaskAppCreator("/path/to/project", templates=custom_templates)
creator.run()
```
## Supported Features

Currently, FlaskFolderStructure supports generating:

1. Application folder with app/ as the core component.
2. Models, routes, schemas, utils, and test folder scaffolding.
3. Customizable template-based file generation.

## Contributing

Contributions are welcome! If you encounter any issues, have feature requests, or would like to contribute code, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

This project was inspired by common Flask project structures and aims to simplify the process of setting up new Flask applications.