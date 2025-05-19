import math

def calculate_term(x, k):
    power = 2 * k - 1
    return 2 * (x ** power) / power

def generate_taylor_terms(x, max_terms=100):
    k = 1
    while k <= max_terms:
        yield calculate_term(x, k)
        k += 1

def calculate_with_taylor_series(x, epsilon):
    if abs(x) >= 1:
        print("Error: |x| must be less than 1 for this series to converge")
        return None
    
    result = 0
    k = 1
    term = calculate_term(x, k)
    
    while abs(term) >= epsilon:
        result += term
        k += 1
        term = calculate_term(x, k)
    
    return result

x = float(input("Enter value for x (|x| < 1): "))
epsilon = float(input("Enter accuracy (epsilon): "))

if abs(x) < 1:
    taylor_result = calculate_with_taylor_series(x, epsilon)
    exact_result = math.log((1 + x) / (1 - x))
    
    print(f"First few terms of Taylor series:")
    terms_count = 5
    for i, term in enumerate(generate_taylor_terms(x, terms_count), 1):
        print(f"Term {i}: {term}")
    
    print(f"\nResult using Taylor series with accuracy {epsilon}: {taylor_result}")
    print(f"Result using math.log((1+x)/(1-x)): {exact_result}")
    print(f"Absolute difference: {abs(taylor_result - exact_result)}")
else:
    print("Error: |x| must be less than 1 for this series to converge") 