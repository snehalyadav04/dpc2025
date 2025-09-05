def find_largest_with_k_occurrences(arr, k):
    unique_elements = set(arr)
    valid_elements = [x for x in unique_elements if arr.count(x) == k]
    
    if not valid_elements:
        return -1
    return max(valid_elements)

arr = [2, 3, 4, 2, 2, 5, 5]
k = 2
print("Input: arr =", arr, ", k =", k)
print("Output:", find_largest_with_k_occurrences(arr, k))

arr = [1, 1, 1, 1]
k = 1
print("Input: arr =", arr, ", k =", k)
print("Output:", find_largest_with_k_occurrences(arr, k))

arr = [10]
k = 1
print("Input: arr =", arr, ", k =", k)
print("Output:", find_largest_with_k_occurrences(arr, k))

arr = [6, 6, 6, 6, 7, 7, 8, 8, 8]
k = 3
print("Input: arr =", arr, ", k =", k)
print("Output:", find_largest_with_k_occurrences(arr, k))
