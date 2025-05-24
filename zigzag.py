print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
import time

def zigzag():
    indent = 0
    indent_increasing = True
    zigzag_count = 0
    max_zigzags = 3  

    print("Welcome to the Zigzag pattern! It will stop after 5 zigzags.\n")
    while zigzag_count < max_zigzags:
        print(' ' * indent + '**')
        time.sleep(0.05)

        if indent_increasing:
            indent += 1
            if indent == 4:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
                zigzag_count += 1

    print("\nZigzag ended. Have a great day!")

zigzag()
