from rational import Rational
from rational_list import RationalList

def process_file(filename):
    numbers = RationalList()
    
    with open(filename, 'r') as file:
        for line in file:
            tokens = line.strip().split()
            for token in tokens:
                if '/' in token:
                    numbers.append(Rational(token))
                else:
                    numbers.append(int(token))
    
    sum_result = Rational(0, 1)
    for i in range(len(numbers)):
        sum_result = sum_result + numbers[i]
    
    return sum_result

input_files = ['input01.txt', 'input02.txt', 'input03.txt']

for filename in input_files:
    try:
        result = process_file(filename)
        print(f"Sum for {filename}: {result}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error processing {filename}: {e}") 