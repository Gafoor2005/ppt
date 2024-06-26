def count_valleys(steps, hike_sequence): sea_level = 0 # Starting at sea level
    valleys = 0
    in_valley = False
    for step in hike_sequence:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1
    if step == 'U' and sea_level == 0:
        if in_valley:
            valleys += 1
        in_valley = False
    elif step == 'D' and sea_level < 0:
        in_valley = True
    return valleys