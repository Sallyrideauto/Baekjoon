# https://sunchol21.tistory.com/345
# math 모듈에 대한 추가 학습 필요(시간 초과 문제와 연관이 있어 보임)

import math

N = int(input())
cnt = 0

for i in range(1, int (math.sqrt(N)) + 1):
    if N % i == 0:
        if (N // i) == i:
            cnt += 1
        else:
            cnt += 2

print(cnt)