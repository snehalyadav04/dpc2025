def find_output(arr):
    n = len(arr)
    stack = []
    max_right = arr[-1]
    stack.append(max_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            stack.append(max_right)

    return stack[::-1]
test_cases = [
    [1, 2, 3, 4, 0],
    [7, 10, 4, 10, 6, 5, 2],
    [5],
    [100, 50, 20, 10],
    list(range(1, 1000001))
]
for arr in test_cases:
    Output = find_output(arr)
    if len(arr) > 20:
        print(f"Input: [1, 2, 3, ..., {arr[-1]}]") 
    else:
        print(f"Input: {arr}")
    print(f"Output: {Output}\n")
