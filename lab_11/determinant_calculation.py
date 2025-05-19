def calculate_determinant_recursive(n, a, b):
    if n == 1:
        return a + b
    if n == 2:
        return (a + b) ** 2 - a * b
    
    d_prev = calculate_determinant_recursive(n - 1, a, b)
    d_prev_prev = calculate_determinant_recursive(n - 2, a, b)
    
    return (a + b) * d_prev - a * b * d_prev_prev

def generate_determinants(max_n, a, b):
    n = 1
    while n <= max_n:
        yield calculate_determinant_with_loop(n, a, b)
        n += 1

def calculate_determinant_with_loop(n, a, b):
    if n == 1:
        return a + b
    
    d_prev_prev = a + b 
    d_prev = (a + b) ** 2 - a * b 
    
    for i in range(3, n + 1):
        d_current = (a + b) * d_prev - a * b * d_prev_prev
        d_prev_prev = d_prev
        d_prev = d_current
    
    return d_prev if n > 1 else d_prev_prev

n = int(input("Enter value for n (order of determinant): "))
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

print(f"Determinant of order {n} with a={a} and b={b}:")
result = calculate_determinant_with_loop(n, a, b)
print(f"Result: {result}")

print(f"Sequence of determinants from order 1 to {n}:")
for i, det in enumerate(generate_determinants(n, a, b), 1):
    print(f"Order {i}: {det}") 