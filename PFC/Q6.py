def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_ascii_values(s): 
    return sum(ord(char) for char in s)
def is_prime_string(s): 
    ascii_sum = sum_ascii_values(s)
    return is_prime(ascii_sum)