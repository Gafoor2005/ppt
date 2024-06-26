def find_peak_element(arr): 
    left, right = 0, len(arr) - 1
    while left < right: 
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]: 
            right = mid 
        else: 
            left = mid + 1
    # At the end of the loop, left and right will be equal, and pointing to a peak element 
    return left