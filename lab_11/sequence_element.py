import math

def calculate_element(x, k):
    numerator = x ** (2 * k)
    denominator = math.factorial(2 * k)
    return numerator / denominator

def generate_sequence(x, count):
    k = 0
    while k < count:
        yield calculate_element(x, k)
        k += 1

def get_element_with_loop(x, k):
    result = 0
    for i in range(k + 1):
        result = x ** (2 * i) / math.factorial(2 * i)
    return result

x = float(input("Enter value for x: "))
k = int(input("Enter value for k: "))

print(f"Element x_{k} = {calculate_element(x, k)}")

print("First", k+1, "elements of the sequence:")
for i, element in enumerate(generate_sequence(x, k+1)):
    print(f"x_{i} = {element}")

print(f"Element calculated with loop: {get_element_with_loop(x, k)}") 