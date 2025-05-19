from rational import Rational
from rational_list import RationalList
from rational_exceptions import RationalError, RationalValueError

def test_rational_error():
    print("Testing RationalError:")
    try:
        # Try to create a Rational with zero denominator
        r = Rational(1, 0)
    except RationalError as e:
        print(f"Caught RationalError: {e}")
    
    try:
        # Try to set denominator to zero
        r = Rational(1, 2)
        r["d"] = 0
    except RationalError as e:
        print(f"Caught RationalError when setting d to 0: {e}")
    
    try:
        # Try to divide by zero
        r1 = Rational(1, 2)
        r2 = Rational(0, 1)
        r3 = r1 / r2
    except RationalError as e:
        print(f"Caught RationalError during division: {e}")

def test_rational_value_error():
    print("\nTesting RationalValueError:")
    r = Rational(1, 2)
    
    try:
        # Try to add incompatible type
        result = r + "string"
    except RationalValueError as e:
        print(f"Caught RationalValueError during addition: {e}")
    
    try:
        # Try to subtract incompatible type
        result = r - [1, 2]
    except RationalValueError as e:
        print(f"Caught RationalValueError during subtraction: {e}")
    
    try:
        # Try to multiply by incompatible type
        result = r * {"a": 1}
    except RationalValueError as e:
        print(f"Caught RationalValueError during multiplication: {e}")
    
    try:
        # Try to divide by incompatible type
        result = r / 3.14
    except RationalValueError as e:
        print(f"Caught RationalValueError during division: {e}")

def test_rational_list_value_error():
    print("\nTesting RationalValueError in RationalList:")
    rl = RationalList()
    
    try:
        # Try to append incompatible type
        rl.append("string")
    except RationalValueError as e:
        print(f"Caught RationalValueError during append: {e}")
    
    try:
        # Try to set incompatible type
        rl.append(Rational(1, 2))
        rl[0] = 3.14
    except RationalValueError as e:
        print(f"Caught RationalValueError during item assignment: {e}")
    
    try:
        # Try to add incompatible list
        rl2 = rl + [1, 2, 3]
    except RationalValueError as e:
        print(f"Caught RationalValueError during list addition: {e}")
    
    try:
        # Try to += incompatible type
        rl += 3.14
    except RationalValueError as e:
        print(f"Caught RationalValueError during += operation: {e}")

if __name__ == "__main__":
    test_rational_error()
    test_rational_value_error()
    test_rational_list_value_error() 