def prime_factors(N):
    factors = []
    
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    i = 3
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N //= i
        i += 2

    if N > 2:
        factors.append(N)

    return factors

test_cases = [
    30,        
    49,        
    19,        
    64,        
    123456     
]

for N in test_cases:
    result = prime_factors(N)
    print(f"Input: N = {N}")
    print(f"Output: {result}")
    print()
