def findDuplicate(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow
test_cases = [
    [1, 3, 4, 2, 2],                         
    [3, 1, 3, 4, 2],                         
    [1, 1],                                  
    [1, 4, 4, 2, 3],                        
    list(range(1, 100000)) + [50000]        
]
for i, arr in enumerate(test_cases, 1):
    print(f"Test Case {i}")
    display_input = arr if len(arr) <= 20 else arr[:10] + ["..."]
    print(f"Input: {display_input}")
    print(f"Output: {findDuplicate(arr)}")
    print()
