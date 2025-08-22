def reverse_words(s: str) -> str:
    words = s.strip().split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

test_cases = [
    "the sky is blue",
    "  hello world  ",
    "a good   example",
    "    ",
    "word"
]

for s in test_cases:
    output = reverse_words(s)
    print(f'Input: "{s}"')
    print(f'Output: "{output}"\n')
