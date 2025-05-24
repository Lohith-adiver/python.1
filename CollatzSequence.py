print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
def collatz(n):
    while n != 1:
        print(n, end=' --> ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

try:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        print("Collatz sequence:")
        collatz(num)
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
