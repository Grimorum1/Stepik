import time
class DeltaClock:

    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        res = self.clock1.get_time()-self.clock2.get_time()
        if res<0:
            return  f'00: 00: 00'
        else:
            return time.strftime('%H: %M: %S', time.gmtime(res))

    def __len__(self):
        return self.clock1.get_time()-self.clock2.get_time()




class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def get_time(self):
        return (self.hours * 3600 + self.minutes * 60 + self.seconds)

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)