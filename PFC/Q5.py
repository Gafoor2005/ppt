def find_min_balance_value(arr):
    total_sum = sum(arr)
    target_sum = total_sum // 2
    left_sum = 0
    for element in arr:
        left_sum += element
        if left_sum >= target_sum: 
            return left_sum - target_sum