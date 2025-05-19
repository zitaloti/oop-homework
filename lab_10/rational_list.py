from rational import Rational

class RationalList:
    def __init__(self):
        self.numbers = []
    
    def __getitem__(self, index):
        return self.numbers[index]
    
    def __setitem__(self, index, value):
        if isinstance(value, (int, Rational)):
            if isinstance(value, int):
                value = Rational(value, 1)
            self.numbers[index] = value
        else:
            raise TypeError("Only Rational or int values are allowed")
    
    def __len__(self):
        return len(self.numbers)
    
    def append(self, value):
        if isinstance(value, (int, Rational)):
            if isinstance(value, int):
                value = Rational(value, 1)
            self.numbers.append(value)
        else:
            raise TypeError("Only Rational or int values are allowed")
    
    def __add__(self, other):
        result = RationalList()
        result.numbers = self.numbers.copy()
        
        if isinstance(other, RationalList):
            result.numbers.extend(other.numbers)
        elif isinstance(other, (int, Rational)):
            if isinstance(other, int):
                other = Rational(other, 1)
            result.numbers.append(other)
        else:
            raise TypeError("Can only concatenate with RationalList, Rational or int")
        
        return result
    
    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.numbers.extend(other.numbers)
        elif isinstance(other, (int, Rational)):
            if isinstance(other, int):
                other = Rational(other, 1)
            self.numbers.append(other)
        else:
            raise TypeError("Can only concatenate with RationalList, Rational or int")
        
        return self 