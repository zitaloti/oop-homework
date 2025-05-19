class RationalError(ZeroDivisionError):
    def __init__(self, message="Denominator cannot be zero"):
        self.message = message
        super().__init__(self.message)

class RationalValueError(Exception):
    def __init__(self, message="Invalid data for rational number operation"):
        self.message = message
        super().__init__(self.message) 