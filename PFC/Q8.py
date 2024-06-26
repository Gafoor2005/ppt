def trapped_water(arr): 
    n = len(arr) 
    left_max = [0] * n
    right_max = [0] * n
    total_water = 0

    # Calculate the maximum height from the left for each block 
    left_max[0] = arr[0] 
    for i in range(1, n): 
        left_max[i] = max(left_max[i - 1], arr[i])

    # Calculate the maximum height from the right for each block 
    right_max[n-1] = arr[n - 1] 
    for i in range(n -2, -1, -1): 
        right_max[i] = max(right_max[i + 1], arr[i])

    # Calculate the trapped water for each block and sum them up 
    for i in range(n): 
        trapped_water = min(left_max[i], right_max[i]) - arr[i] 
        total_water += trapped_water
    return total_water