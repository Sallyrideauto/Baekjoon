def solution(x):
    sum_val = sum(map(int, str(x)))
    if x % sum_val == 0:
        return True
    else:
        return False