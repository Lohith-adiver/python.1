print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

import os

threshold_mb = 100
threshold_bytes = threshold_mb * 1024 * 1024
found = 0

for foldername, _, filenames in os.walk('.'):
    for file in filenames:
        filepath = os.path.join(foldername, file)
        try:
            if os.path.getsize(filepath) > threshold_bytes:
                print(os.path.abspath(filepath))
                found += 1
        except (PermissionError, FileNotFoundError):
            continue

print(f"Done. Found {found} file(s) larger than {threshold_mb}MB.")
