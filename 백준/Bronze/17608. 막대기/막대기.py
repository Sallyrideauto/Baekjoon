'''
제시된 문제를 효율적으로 해결하기 위해서는 막대기를 입력받으면서 동시에 최대 높이를 업데이트하고,
이를 통해 보이는 막대기의 수를 계산하는 알고리즘을 사용해야 합니다.
이전의 코드는 중복된 높이의 막대기를 필터링하는 데 시간을 소모하고 있으며,
모든 막대기의 높이를 비교하는 방식은 시간 복잡도가 높아 매우 비효율적입니다.

최적화된 방법은 다음과 같습니다:
1. 입력 받은 막대기의 높이를 배열에 저장합니다.
2. 배열의 마지막부터 시작하여 현재까지의 최대 높이를 기록합니다.
3. 현재 막대기의 높이가 현재까지의 최대 높이보다 크면, 보이는 막대기의 수를 증가시킵니다.
'''

import sys

N = int(input())
heights = [int(sys.stdin.readline().strip()) for _ in range(N)]

count = 0
max_height = 0

# 오른쪽부터 확인하면서 막대기 개수 세기
for h in reversed(heights):
    if h > max_height:
        count += 1
        max_height = h

print(count)

'''
이 알고리즘은 각 막대기를 한 번씩만 확인하므로 시간 복잡도는 O(N)이 됩니다. 
입력받는 부분에서 sys.stdin.readline()을 사용해 입력 속도를 향상시키고, 
출력은 단 한 번만 하기 때문에 시간 초과 문제를 해결할 수 있습니다.
'''
