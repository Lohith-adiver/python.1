print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
import random

number_of_experiments = 10000
streak_length = 6
streaks_found = 0

for _ in range(number_of_experiments):
    flips = []
    for i in range(100):  
        flips.append(random.choice(['H', 'T']))


    for i in range(len(flips) - streak_length + 1):
        if all(f == flips[i] for f in flips[i:i + streak_length]):
            streaks_found += 1
            break  
print(f"Streaks of {streak_length} found in {streaks_found} out of {number_of_experiments} experiments.")
print(f"Chance of streak: {streaks_found / number_of_experiments * 100:.2f}%")
