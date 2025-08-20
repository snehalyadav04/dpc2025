from collections import defaultdict

def find_zero_sum_subarrays(arr):
    prefix_sum_map = defaultdict(list)
    prefix_sum_map[0].append(-1)  
    result = []
    prefix_sum = 0

    for index, value in enumerate(arr):
        prefix_sum += value

        if prefix_sum in prefix_sum_map:
            for start_index in prefix_sum_map[prefix_sum]:
                result.append((start_index + 1, index))

        prefix_sum_map[prefix_sum].append(index)

    return result


test_cases = [
    {
        "input": [4, -1, -3, 1, 2, -1],
        "expected": [(1, 2), (0, 3)]
    },
    {
        "input": [1, 2, 3, 4],
        "expected": []
    },
    {
        "input": [0, 0, 0],
        "expected": [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    },
    {
        "input": [-3, 1, 2, -3, 4, 0],
        "expected": [(0, 3), (4, 4)]
    },
    {
        "input": [1, -1, 2, -2, 3, -3] * 10000,
        "expected_partial": [(0, 1), (2, 3), (4, 5)]  
    }
]


for idx, case in enumerate(test_cases):
    print(f"Input {idx+1}: {case['input'][:20]}{'...' if len(case['input']) > 20 else ''}")
    result = find_zero_sum_subarrays(case['input'])

    if idx == 4:  
        print(f"Output {idx+1}: First 10 results: {result[:10]}")
        print(f"Total zero-sum subarrays: {len(result)}")
    else:
        print(f"Output {idx+1}: {result}")
    print()
