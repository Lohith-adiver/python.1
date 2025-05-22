print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
import time

def zigzag():
    indent = 0
    indent_increasing = True

    try:
        print("Welcome to the Zigzag pattern! Press Ctrl+C to stop.\n")
        while True:
            print(' ' * indent + '🌟')
            time.sleep(0.05)

            if indent_increasing:
                indent += 1
                if indent == 20:
                    indent_increasing = False
            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        print("\nZigzag ended. Have a great day!")

zigzag()
