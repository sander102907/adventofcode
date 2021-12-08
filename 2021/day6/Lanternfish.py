class Lanternfish:
    def __init__(self, timer=8):
        self.timer = timer

    # update internal timer of lanternfish and return whether a new lanternfish is produced
    def new_day(self):
        self.timer -= 1

        if self.timer < 0:
            self.timer = 6
            return True

        return False

    def __repr__(self) -> str:
        return str(self.timer)