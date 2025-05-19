class Rational:
    def __init__(self, n, d=None):
        if d is None and isinstance(n, str):
            parts = n.split('/')
            n = int(parts[0])
            d = int(parts[1])
        
        if d == 0:
            raise ValueError("Denominator cannot be zero")
            
        def gcd(a, b):
            a = abs(a)
            b = abs(b)
            while b:
                a, b = b, a % b
            return a
            
        divisor = gcd(n, d)
        self.n = n // divisor
        self.d = d // divisor
        
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.n * other.n, self.d * other.d)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if other.n == 0:
            raise ValueError("Division by zero")
        return Rational(self.n * other.d, self.d * other.n)
    
    def __call__(self):
        return self.n / self.d
    
    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        raise KeyError("Only 'n' and 'd' keys are supported")
    
    def __setitem__(self, key, value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ValueError("Denominator cannot be zero")
            self.d = value
        else:
            raise KeyError("Only 'n' and 'd' keys are supported")
    
    def __str__(self):
        return f"{self.n}/{self.d}" 