def count_buildings_with_sunrise(arr):
    n = len(arr)
    visible_buildings = 0
    max_height = 0
    for height in arr:
        if height > max_height:
        visible_buildings += 1 
        max_height = height
    return visible_buildings