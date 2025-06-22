print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.seconds = hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

def mul_time(time, number):
    return Time(0, 0, int(time.seconds * number))

def average_pace(total_time, distance):
    return mul_time(total_time, 1 / distance)


t = Time(1, 10, 0)  # 1 hour 10 minutes = 4200 seconds
d = 10              # 10 km or miles
print("Total time:", t)
print("Average pace per km/mile:", average_pace(t, d))
