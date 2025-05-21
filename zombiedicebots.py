import random

print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

def roll_die():
    return random.choice(['brain', 'shotgun', 'footsteps'])

def bot_turn():
    brains = 0
    shotguns = 0
    roll_number = 0

    while True:
        roll_number += 1
        print("\nRoll", roll_number)
        dice = [roll_die(), roll_die(), roll_die()]
        print("Dice rolled:", dice)

        for die in dice:
            if die == 'brain':
                brains += 1
            elif die == 'shotgun':
                shotguns += 1

        print("Brains:", brains, "Shotguns:", shotguns)

        if shotguns >= 3:
            print("Too many shotguns! Lost all brains this turn.")
            brains = 0
            break

        if brains >= 3:
            print("Enough brains, bot decides to stop.")
            break

    print("\nFinal brains this turn:", brains)

bot_turn()
