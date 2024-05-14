import os
from pathlib import Path



def main():

    user_input = input("Enter the directory path where you want to create the Flask app structure: ")
    base_path = Path(user_input)

    # Check if the path exists and is a directory
    if not base_path.exists() or not base_path.is_dir():
        print("Error: The specified path does not exist or is not a directory.")
        return

    

if __name__ == "__main__":
    main()