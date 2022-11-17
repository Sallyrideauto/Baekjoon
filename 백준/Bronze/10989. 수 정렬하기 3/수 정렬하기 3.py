# 추가적으로 정리 필요

import sys

N = int(input())
count_sort = [0] * 10001

for i in range(N):
    count_sort[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count_sort[i] != 0:
        for j in range(count_sort[i]):
            print(i)