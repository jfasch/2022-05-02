import itertools
import random


class CyclicSensor:
    def __init__(self, values_millicelsius):
        self.values_iterator = iter(itertools.cycle(values_millicelsius))
    def get_temperature(self):
        return next(self.values_iterator)


class RandomSensor:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_temperature(self):
        return random.randrange(self.start, self.end)
