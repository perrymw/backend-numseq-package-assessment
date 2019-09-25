def is_prime(n):
    if (n) <= 1 :
        return False
    elif n == 2:
        return True
    else:
        for m in range(2, n):
            if n % m == 0:
                return False
        return True

def prime(n):
    stack = []
    for x in range(1, n + 1):
        if is_prime(x):
            stack.append(x)
    return stack