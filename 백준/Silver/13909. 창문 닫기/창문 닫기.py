import math

def count_open_windows(N):
    return int(math.sqrt(N))
    
N = int(input())
print(count_open_windows(N))