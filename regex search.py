
print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
                                                             
import os, re

pattern = input("Enter a regex pattern: ")
regex = re.compile(pattern)

for filename in os.listdir():
    if filename.endswith('.txt'):
        with open(filename, encoding='utf-8', errors='ignore') as f:
            for line in f:
                if regex.search(line):
                    print(f"{filename}: {line.strip()}")
