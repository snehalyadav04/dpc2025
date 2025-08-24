from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())

test_cases = {
    "Test Case 1": ["eat", "tea", "tan", "ate", "nat", "bat"],
    "Test Case 2": [""],
    "Test Case 3": ["a"],
    "Test Case 4": ["abc", "bca", "cab", "xyz", "zyx", "yxz"],
    "Test Case 5": ["abc", "def", "ghi"]
}

for name, input_case in test_cases.items():
    output = groupAnagrams(input_case)
    print(f"{name}")
    print(f"Input: {input_case}")
    print(f"Output: {output}\n")
