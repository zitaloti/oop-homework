def calculate_a_k(k):
    if k == 1 or k == 2 or k == 3:
        return 1
    
    return calculate_a_k(k - 1) + calculate_a_k(k - 3)

def generate_sequence_terms(n):
    a = [1, 1, 1]
    
    for k in range(4, n + 1):
        a.append(a[k - 2] + a[k - 4]) 
    
    for k in range(1, n + 1):
        yield a[k - 1] / (2 ** k)

def calculate_sum_with_loop(n):
    a = [1, 1, 1]
    
    for k in range(4, n + 1):
        next_term = a[k - 2] + a[k - 4] 
        a.append(next_term)
    
    sum_result = 0
    for k in range(1, n + 1):
        sum_result += a[k - 1] / (2 ** k)
    
    return sum_result

n = int(input("Enter value for n: "))

print(f"Terms of the sum S_{n}:")
for i, term in enumerate(generate_sequence_terms(n), 1):
    print(f"Term {i}: a_{i}/{2**i} = {term}")

sum_result = calculate_sum_with_loop(n)
print(f"S_{n} = {sum_result}") 