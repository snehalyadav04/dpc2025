def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(n, m):
    return n * m // gcd(n, m)

test_cases = [
    (4, 6),
    (5, 10),
    (7, 3),
    (1, 987654321),
    (123456, 789012)
]

for n, m in test_cases:
    result = lcm(n, m)
    print(f"Input: N = {n}, M = {m} = Output: {result}")
