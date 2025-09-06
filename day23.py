from collections import deque

def max_in_subarrays(arr, k):
    n = len(arr)
    if k > n:
        return []

    dq = deque()  
    result = []

    for i in range(n):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

# Test Case 1
arr1 = [1, 5, 3, 2, 4, 6]
k1 = 3
output1 = max_in_subarrays(arr1, k1)
print("Input:", arr1, "k =", k1)
print("Output:", output1)

# Test Case 2
arr2 = [1, 2, 3, 4]
k2 = 2
output2 = max_in_subarrays(arr2, k2)
print("\nInput:", arr2, "k =", k2)
print("Output:", output2)

# Test Case 3
arr3 = [7, 7, 7, 7]
k3 = 1
output3 = max_in_subarrays(arr3, k3)
print("\nInput:", arr3, "k =", k3)
print("Output:", output3)
