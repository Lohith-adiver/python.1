print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
import re
import os

filename = input("Enter the input text filename (e.g., text.txt): ")

if not os.path.exists(filename):
    print(f"❌ File '{filename}' not found.")
    exit()

with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
    content = file.read()

placeholders = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', content)

for word in placeholders:
    replacement = input(f"Enter a {word.lower()}: ")
    content = content.replace(word, replacement, 1)

print("\n✅ Final Story:\n")
print(content)

# Save the modified story to a new file
output_file = "madlib_output.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"\n📝 Output saved to '{output_file}'")
