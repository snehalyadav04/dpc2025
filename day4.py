def merge(arr1, arr2):
    import math
    m, n = len(arr1), len(arr2)
    total = m + n
    gap = math.ceil(total / 2)

    while gap > 0:
        i = 0
        j = gap
        while j < total:
            # Case 1: both in arr1
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # Case 2: i in arr1, j in arr2
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            # Case 3: both in arr2
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        if gap == 1:
            break
        gap = math.ceil(gap / 2)


# ---------- Test Cases ----------
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merge(arr1, arr2)
print("arr1 =", arr1, "arr2 =", arr2)  # ✅ [1,2,3], [4,5,6]

arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
merge(arr1, arr2)
print("arr1 =", arr1, "arr2 =", arr2)  # ✅ [1,3,5], [10,12,14]

arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
merge(arr1, arr2)
print("arr1 =", arr1, "arr2 =", arr2)  # ✅ [2,3,4], [6,8,10]

arr1 = [1]
arr2 = [2]
merge(arr1, arr2)
print("arr1 =", arr1, "arr2 =", arr2)  # ✅ [1], [2]
