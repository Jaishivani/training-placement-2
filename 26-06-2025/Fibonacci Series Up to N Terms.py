def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
terms = int(input("Enter number of terms: "))
fibonacci(terms)
