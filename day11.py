from itertools import permutations

def permute_unique(s):
    return sorted(set([''.join(p) for p in permutations(s)]))

test_inputs = [
    "abc",   
    "aab",   
    "aaa",   
    "a",     
    "abcd"   
]

for test in test_inputs:
    result = permute_unique(test)
    print(f"Input: \"{test}\"")
    print("Output:", result)
