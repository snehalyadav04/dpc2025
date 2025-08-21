def trap(height):
    if len(height) < 3:
        return 0  
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            if height[left] < left_max:
                water_trapped += left_max - height[left]
            else:
                left_max = height[left]
        else:
            right -= 1
            if height[right] < right_max:
                water_trapped += right_max - height[right]
            else:
                right_max = height[right]

    return water_trapped

test_cases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],  
    [4, 2, 0, 3, 2, 5],                   
    [1, 1, 1],                            
    [5],                                 
    [2, 0, 2],                           
]

for height in test_cases:
    result = trap(height)
    print(f"Input: height[] = {height}")
    print(f"Output: {result}")
    print("-" * 40)
