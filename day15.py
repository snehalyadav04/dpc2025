def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Test Case1
s1 = "abcabcbb"
print("Input: S =", s1)
print("Output:", length_of_longest_substring(s1))
print()

# Test Case2
s2 = "bbbbb"
print("Input: S =", s2)
print("Output:", length_of_longest_substring(s2))
print()

# Test Case3
s3 = "pwwkew"
print("Input: S =", s3)
print("Output:", length_of_longest_substring(s3))
print()

# Test Case4
s4 = "abcdefgh"
print("Input: S =", s4)
print("Output:", length_of_longest_substring(s4))
print()

# Test Case5
s5 = "a"
print("Input: S =", s5)
print("Output:", length_of_longest_substring(s5))
