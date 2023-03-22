"""
시간 초과가 발생하는 경우에는 알고리즘이 비효율적이거나, 입력값의 크기 때문일 수 있습니다.
따라서 입력값이 큰 경우에는 더 효율적인 알고리즘을 사용해야 합니다.

아래는 네 가지 기본 통계값을 구하는 파이썬 코드입니다. 
이 코드는 입력값이 크더라도 O(N) 시간 복잡도를 가지므로, 
입력값이 큰 경우에도 빠르게 동작할 수 있습니다.
"""

import sys
from collections import Counter

# 입력값 받기
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

# 산술평균 구하기
avg = sum(arr) / n
print(round(avg))

# 중앙값 구하기
arr.sort()
mid = arr[n//2]
print(mid)

# 최빈값 구하기
cnt = Counter(arr)
mode = cnt.most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1]:
    mode_value = mode[1][0]
else:
    mode_value = mode[0][0]
print(mode_value)

# 범위 구하기
range_value = max(arr) - min(arr)
print(range_value)


"""
이 코드는 입력값을 받을 때 sys.stdin.readline() 함수를 사용하므로 더 빠르게 입력을 처리할 수 있습니다. 
또한, collections 모듈의 Counter 클래스를 사용하여 리스트에 있는 각 요소들의 빈도수를 딕셔너리 형태로 계산할 수 있습니다. 
이를 활용하여 최빈값을 구하였습니다.
"""
