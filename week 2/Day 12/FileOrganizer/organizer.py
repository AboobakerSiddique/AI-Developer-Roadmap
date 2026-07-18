import shutil
from pathlib import Path

# Extension to folder mapping
folders = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".pdf": "PDFs",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".wav": "Music"
}

def organize_files(source_folder="test_folder"):
    """Organize files in source_folder into subfolders based on file extension."""
    source_path = Path(source_folder)
    # If source folder doesn't exist, create it and exit (nothing to organize yet)
    if not source_path.exists():
        source_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {source_path}. Add files and run again.")
        return
    
    # Loop through every file in the folder
    for file_path in source_path.iterdir():
        # Ignore folders, only organize files
        if file_path.is_dir():
            continue
        
        # Get file extension
        extension = file_path.suffix.lower()
        
        # Find destination folder based on extension
        destination_folder = folders.get(extension, "Others")
        
        # Create full destination path
        dest_path = source_path / destination_folder
        
        # Create folder if needed
        dest_path.mkdir(exist_ok=True)
        
        # Move file to destination
        shutil.move(str(file_path), str(dest_path / file_path.name))
        print(f"Moved {file_path.name} to {destination_folder}/")

if __name__ == "__main__":
    organize_files()