'''
# 시도했다 실패한 코드

import math

def solution(n):
    x = int(input())
    double_x = math.sqrt(x)
    if n == double_x:
        return math.sqrt(x + 1)
    else:
        return -1

https://needneo.tistory.com/77
https://1ets-just-do-it.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%95%EC%88%98-%EC%A0%9C%EA%B3%B1%EA%B7%BC-%ED%8C%90%EB%B3%84-Lv1
'''

def solution(n):
    n = n ** (0.5)
    
    if n % 1 == 0:
        return (n + 1) ** 2
    
    return -1