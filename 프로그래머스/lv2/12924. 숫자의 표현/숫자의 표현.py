def solution(n):
    count = 0
    max_start = int((2 * n + 0.25)**0.5 - 0.5) # formula for maximum starting number
    for start in range(1, max_start+1):
        series_sum = (2 * n - start * (start - 1)) / (2 * start)
        if series_sum.is_integer(): # check if series sum is an integer
            count += 1
    return count
