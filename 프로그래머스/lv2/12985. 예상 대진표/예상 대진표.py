def solution(n, a, b):
    round = 0
    while n > 1:
        round += 1
        if abs(a - b) == 1 and max(a, b) % 2 == 0:
            return round
        a = (a + 1) // 2
        b = (b + 1) // 2
        n = n // 2
    return round