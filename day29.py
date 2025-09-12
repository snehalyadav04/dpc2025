def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Test cases
test_inputs = [5, 10, 0, 1000]
for n in test_inputs:
    result = fibonacci(n)
    if n >= 100:
        print(f"Input: {n}\nOutput: {format(result, '.15e')}\n")
    else:
        print(f"Input: {n}\nOutput: {result}\n")
