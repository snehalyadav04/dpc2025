def count_at_most_k_distinct(s: str, k: int) -> int:
    n = len(s)
    freq = {}
    left = 0
    total = 0

    for right in range(n):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        total += right - left + 1

    return total


def count_substrings_with_exactly_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    return count_at_most_k_distinct(s, k) - count_at_most_k_distinct(s, k - 1)

print("Test Case 1")
s = "pqpqs"
k = 2
print("Input: s =", s, ", k =", k)
print("Output:", count_substrings_with_exactly_k_distinct(s, k))  

print("\nTest Case 2")
s = "aabacbebebe"
k = 3
print("Input: s =", s, ", k =", k)
print("Output:", count_substrings_with_exactly_k_distinct(s, k))  

print("\nTest Case 3")
s = "a"
k = 1
print("Input: s =", s, ", k =", k)
print("Output:", count_substrings_with_exactly_k_distinct(s, k))  

print("\nTest Case 4")
s = "abc"
k = 3
print("Input: s =", s, ", k =", k)
print("Output:", count_substrings_with_exactly_k_distinct(s, k))  

print("\nTest Case 5")
s = "abc"
k = 2
print("Input: s =", s, ", k =", k)
print("Output:", count_substrings_with_exactly_k_distinct(s, k)) 
