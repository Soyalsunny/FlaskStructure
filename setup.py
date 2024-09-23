from setuptools import setup, find_packages

setup(
    name="flask_folder_creator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0',  
    ],
    entry_points={
        'console_scripts': [
            'create_flask_structure=flask_folder_creator.creator:create_structure', 
        ],
    },
    author="Soyal",
    author_email="ysoyal@qburst.com",
    description="A package to create Flask folder structures",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
