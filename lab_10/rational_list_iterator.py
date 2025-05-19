from rational import Rational

class RationalListIterator:
    def __init__(self, numbers):
        self.numbers = sorted(numbers, key=lambda x: (-x.d, -x.n))
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value 