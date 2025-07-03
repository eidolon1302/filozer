import argparse
import os
import shutil
from datetime import datetime, timedelta
import pyfiglet

def organize_files(source_dir):
    print(f"Organizing files in: {source_dir}")
    if not os.path.isdir(source_dir):
        print(f"Error: Directory not found at {source_dir}")
        return

    # Define categories and their extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".dmg", ".app"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".h", ".php", ".rb", ".go", ".ts"],
    }

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in categories.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(source_dir, category)
                    os.makedirs(destination_folder, exist_ok=True)
                    try:
                        shutil.move(file_path, os.path.join(destination_folder, filename))
                        print(f"Moved '{filename}' to '{category}/'")
                        moved = True
                        break
                    except Exception as e:
                        print(f"Error moving '{filename}': {e}")
            if not moved:
                print(f"Skipped '{filename}': No category found for extension '{file_extension}'")
        elif os.path.isdir(file_path):
            print(f"Skipped directory: '{filename}'")

    print("File organization complete.")

def clean_files(source_dir, days_old=30, dry_run=False):
    print(f"Cleaning files in: {source_dir}")
    if not os.path.isdir(source_dir):
        print(f"Error: Directory not found at {source_dir}")
        return

    cutoff_date = datetime.now() - timedelta(days=days_old)
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            try:
                modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if modified_time < cutoff_date:
                    if dry_run:
                        print(f"Dry run: Would delete old file '{filename}' (last modified: {modified_time.strftime('%Y-%m-%d')})")
                    else:
                        os.remove(file_path)
                        print(f"Deleted old file '{filename}' (last modified: {modified_time.strftime('%Y-%m-%d')})")
                else:
                    print(f"Kept recent file '{filename}' (last modified: {modified_time.strftime('%Y-%m-%d')})")
            except Exception as e:
                print(f"Error processing '{filename}': {e}")
        elif os.path.isdir(file_path):
            # Optionally, you could add logic here to clean empty directories
            print(f"Skipped directory: '{filename}'")

    print("File cleaning complete.")


def main():
    parser = argparse.ArgumentParser(description="A CLI tool to organize and clean files.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=False)

    # Organize command
    organize_parser = subparsers.add_parser("organize", help="Organize files into categorized subfolders.")
    organize_parser.add_argument("directory", nargs="?", default=".", help="The directory to organize. Defaults to current directory.")
    
    # Clean command
    clean_parser = subparsers.add_parser("clean", help="Clean old files from a directory.")
    clean_parser.add_argument("directory", nargs="?", default=".", help="The directory to clean. Defaults to current directory.")
    clean_parser.add_argument("--days-old", type=int, default=30, help="Delete files older than this many days. Default is 30.")
    clean_parser.add_argument("--dry-run", action="store_true", help="Simulate cleaning without actually deleting files.")

    args = parser.parse_args()

    if args.command is None:
        ascii_banner = pyfiglet.figlet_format("File Organizer")
        print(ascii_banner)
        parser.print_help()
        import sys
        sys.exit(1)
    elif args.command == "organize":
        organize_files(os.path.abspath(args.directory))
    elif args.command == "clean":
        clean_files(os.path.abspath(args.directory), args.days_old, args.dry_run)

if __name__ == "__main__":
    main()
