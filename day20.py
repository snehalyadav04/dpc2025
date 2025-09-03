def sort_list(arr):
    return sorted(arr)

test_cases = [
    [7, 1, 5],
    [5],
    [-3, 14, 8, 2],
    [],
    [3, 3, 3]
]

for i, case in enumerate(test_cases, 1):
    result = sort_list(case)
    print(f"Input: {case}")
    print(f"Output: {result}\n")
