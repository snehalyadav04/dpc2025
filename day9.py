def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

test_cases = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["apple", "ape", "april"],
    [""],
    ["alone"]
]

for i, strs in enumerate(test_cases, 1):
    print(f"Example {i}")
    print(f"Input: strs[] = {strs}")
    print(f"Output: \"{longest_common_prefix(strs)}\"\n")
