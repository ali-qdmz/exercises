class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def isEqual (self, other):
        return self.hour == other.hour and self.minute == other.minute and self.second == other.second

