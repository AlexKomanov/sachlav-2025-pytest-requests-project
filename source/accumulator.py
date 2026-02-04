class Accumulator:
    def __init__(self):
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def add_accum(self, num=1):
        self.__count += num