class Lanternfishes:
    def __init__(self, initial_timers):
        # A dictionary where each key is a timer and the value is the number of lanternfishes
        self.timers = {0:0 , 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

        for timer in initial_timers:
            self.timers[timer] += 1

    def new_day(self):
        temp_timers = self.timers.copy()

        for t in range(1, len(self.timers)):
            self.timers[t-1] = self.timers[t]

        self.timers[8] = temp_timers[0]
        self.timers[6] += temp_timers[0]

    def get_total_lanternfishes(self):
        return sum(list(self.timers.values()))
            

