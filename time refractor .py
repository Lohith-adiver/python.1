print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

class Time:
    def __init__(self, seconds=0):
        self.seconds = seconds

    def __str__(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        secs = self.seconds % 60
        return f"{hours:02}:{minutes:02}:{secs:02}"

    def add_time(self, other):
        return Time(self.seconds + other.seconds)

    def is_after(self, other):
        return self.seconds > other.seconds

def int_to_time(seconds):
    return Time(seconds)

def time_to_int(time):
    return time.seconds

# Example usage
t1 = Time(3600 + 30 * 60)  # 01:30:00
t2 = Time(45 * 60)         # 00:45:00

print("Time 1:", t1)
print("Time 2:", t2)

t3 = t1.add_time(t2)
print("Added Time:", t3)
