print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

num = int(input("Enter a number to print its multiplication table: "))
limit = int(input("Multiply till which number? "))

print("Multiplication Table for", num, "up to", limit)
for i in range(1, limit + 1):
    print(num, "x", i, "=", num * i)
