def encode(s):
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)): 
        if s[i] == s[i - 1]:
            count += 1 
        else: 
            count = 1
    result += s[i - 1] + str(count)
    # Add the last character and its count to the result result += s[-1] + str(count)
    return result