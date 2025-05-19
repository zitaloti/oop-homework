def calculate_term(i):
    return 1 + 1 / (i ** 2)

def generate_product_terms(n):
    i = 1
    while i <= n:
        yield calculate_term(i)
        i += 1

def calculate_product_with_loop(n):
    product = 1
    for i in range(1, n + 1):
        term = 1 + 1 / (i ** 2)
        product *= term
    return product

n = int(input("Enter value for n: "))

print(f"Terms of the product:")
for i, term in enumerate(generate_product_terms(n), 1):
    print(f"Term {i}: {term}")

product = calculate_product_with_loop(n)
print(f"P_{n} = {product}") 