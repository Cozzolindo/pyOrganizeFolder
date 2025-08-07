import os # Provides functions for interacting with the operating system, such as file and directory operations.
import shutil # Offers high-level file operations like copying and moving files or directories.
from pathlib import Path # Imports the Path class for object-oriented filesystem paths, making it easier to work with files and directories.


"""
Created by Carlos Cozzolino

How to create an exec file in py:
1. Install pip install pyinstaller
2. Generate exec file with pyinstaller --onefile pyOrganizer.py, after testing the script.

"""
def organize_files():
    """
    Organize files in the current directory by their file types.
    Creates folders for different file types and moves files accordingly.
    """
    
    # Get the current directory where the script is executing
    current_dir = Path.cwd()
    
    # Define file type categories and their extensions
    file_categories = {
        'VIDEO': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg'],
        'AUDIO': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
        'IMAGE': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico'],
        'DOCUMENT': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'],
        'SPREADSHEET': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
        'PRESENTATION': ['.ppt', '.pptx', '.odp', '.key'],
        'ARCHIVE': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        'EXECUTABLE': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.app'],
        'CODE': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.rs'],
        'DATA': ['.json', '.xml', '.yaml', '.yml', '.sql', '.db', '.sqlite']
    }
    
    print(f"Organizing files in: {current_dir}")
    
    # Get all files in the current directory (excluding subdirectories)
    files = [f for f in current_dir.iterdir() if f.is_file() and f.name != os.path.basename(__file__)]
    
    if not files:
        print("No files to organize in the current directory.")
        return
    
    print(f"Found {len(files)} files to organize.")
    
    # Track moved files for summary
    moved_files = {}
    
    for file_path in files:
        file_extension = file_path.suffix.lower()
        
        # Find the category for this file extension
        category = None
        for cat, extensions in file_categories.items():
            if file_extension in extensions:
                category = cat
                break
        
        # If no category found, put in OTHERS folder
        if not category:
            category = 'OTHERS'
        
        # Create category folder if it doesn't exist
        category_folder = current_dir / category
        category_folder.mkdir(exist_ok=True)
        
        # Move the file to the appropriate folder
        destination = category_folder / file_path.name
        
        # Handle file name conflicts
        counter = 1
        original_destination = destination
        while destination.exists():
            name_without_ext = original_destination.stem
            extension = original_destination.suffix
            destination = category_folder / f"{name_without_ext}_{counter}{extension}"
            counter += 1
        
        try:
            shutil.move(str(file_path), str(destination)) # Move the file from file_path to the destination
            
            # Track moved files
            if category not in moved_files:
                moved_files[category] = []
            moved_files[category].append(file_path.name)
            
            print(f"Moved '{file_path.name}' to {category}/ folder")
            
        except Exception as e:
            print(f"Error moving '{file_path.name}': {e}")
    
    # Print summary
    print("\n" + "="*50)
    print("ORGANIZATION SUMMARY")
    print("="*50)

    # Print details of moved files by category
    for category, files in moved_files.items():
        print(f"\n{category} ({len(files)} files):")
        for file in files:
            print(f"  - {file}")
    
    print(f"\nTotal files organized: {sum(len(files) for files in moved_files.values())}")


def main():
    """
    Main function to run the file organizer.
    """
    print("File Organizer - Organize files by type")
    print("-" * 40)
    
    # Ask for user confirmation
    response = input("Do you want to organize files in the current directory? (y/n): ")
    
    if response.lower() in ['y', 'yes']:
        organize_files()
        print("\nFile organization completed!")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()