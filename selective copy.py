print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

import os
import shutil

ext = input("Enter the file extension to search for (e.g., .pdf, .jpg): ").strip()
dest_folder = input("Enter the name of the destination folder: ").strip()

os.makedirs(dest_folder, exist_ok=True)

files_copied = 0
files_skipped = 0

for foldername, _, filenames in os.walk('.'):
    for file in filenames:
        if file.lower().endswith(ext.lower()):
            source_path = os.path.join(foldername, file)
            dest_path = os.path.join(dest_folder, file)
            if os.path.abspath(source_path) != os.path.abspath(dest_path):
                try:
                    shutil.copy(source_path, dest_path)
                    files_copied += 1
                except PermissionError:
                    files_skipped += 1

print(f"Done. {files_copied} file(s) copied to '{dest_folder}'.")
if files_skipped:
    print(f"{files_skipped} file(s) were skipped due to permission errors.")
