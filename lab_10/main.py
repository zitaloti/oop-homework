from rational import Rational
from rational_list_extended import RationalListExtended

def process_file(filename):
    numbers = RationalListExtended()
    
    with open(filename, 'r') as file:
        for line in file:
            tokens = line.strip().split()
            for token in tokens:
                if '/' in token:
                    numbers.append(Rational(token))
                else:
                    numbers.append(int(token))
    return numbers

input_files = ['input01.txt', 'input02.txt', 'input03.txt']

for filename in input_files:
    try:
        numbers = process_file(filename)
        print(f"\nSorted numbers from {filename}:")
        for number in numbers:
            print(number, end=' ')
        print()
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error processing {filename}: {e}") 