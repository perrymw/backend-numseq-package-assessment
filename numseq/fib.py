def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n) + fibonacci(n-1)