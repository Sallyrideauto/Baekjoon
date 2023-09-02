# https://inni-iii.tistory.com/13

import math

def solution(n, m):
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) and (m % i == 0):
            a = i
            break
    for j in range(max(n, m), (n * m) + 1):
        if j % n == 0 and j % m == 0:
            b = j
            break

    return [a, b]