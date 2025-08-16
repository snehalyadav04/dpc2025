def find_missing_number_sum(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum
test_cases = [
    [1, 2, 4, 5],
    [2, 3, 4, 5],
    [1, 2, 3, 4],
    [1],
    list(range(1, 1000000))
]
for arr in test_cases:
    if len(arr) > 20:
        print("Input: [1, 2, 3, ..., 999999]")
    else:
        print(f"Input: {arr}")
    print(f"Output: {find_missing_number_sum(arr)}\n")
