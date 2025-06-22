print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

import os
import re

prefix = input("Enter the file prefix (e.g., spam): ").strip()
extension = input("Enter the file extension (e.g., .txt): ").strip()

pattern = re.compile(rf'{re.escape(prefix)}(\d+){re.escape(extension)}')
files = []

for file in os.listdir():
    match = pattern.fullmatch(file)
    if match:
        files.append((int(match.group(1)), file))

files.sort()
expected = 1

for number, filename in files:
    if number != expected:
        new_name = f"{prefix}{expected:03}{extension}"
        os.rename(filename, new_name)
    expected += 1

print("Gap filling complete.")
