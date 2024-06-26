def calculate_ugliness(N, S, CASH, A, B):
    max_ugliness = int(S, 2) # Calculate the initial ugliness from the binary string
    # Try flip operation and update max_ugliness if it increases
    for bit in S:
        if bit == '1':
            max_ugliness = max(max_ugliness - (2** (N-1)), max_ugliness)
            CASH -= B
    # Try swap operation and update max_ugliness if it increases
    for i in range(N-1):
        if S[i] != S[i + 1]:
            max_ugliness = max(max_ugliness + (2** (N-i-1)) - (2** (N-i-2)) - (2** (N- i - 2)),max_ugliness)
            CASH -= A
    return max_ugliness