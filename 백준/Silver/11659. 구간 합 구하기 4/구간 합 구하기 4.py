"""
먼저, 시간 초과를 해결하기 위해서는 입력 받은 수열의 합을 빠르게 계산할 수 있는 방법이 필요합니다. 
이를 위해 세그먼트 트리를 이용하면 빠르게 수열의 합을 계산할 수 있습니다.

다음은 세그먼트 트리를 이용한 코드입니다. 
이 코드는 입력 받은 수열의 합을 미리 계산해 놓고, 
i부터 j까지의 합을 구할 때는 세그먼트 트리를 이용하여 빠르게 계산합니다.
"""

import sys

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def query(node, start, end, i, j):
    if i > end or j < start:
        return 0
    if i <= start and j >= end:
        return tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, i, j) + query(node*2+1, mid+1, end, i, j)

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 세그먼트 트리 초기화
tree = [0] * (4*N)
init(1, 0, N-1)

# 구간 합 계산
for _ in range(M):
    i, j = map(int, input().split())
    print(query(1, 0, N-1, i-1, j-1))

"""
세그먼트 트리를 이용하면 각 쿼리마다 O(N)이 아니라 
O(logN)의 시간 복잡도로 구간 합을 계산할 수 있으므로, 
시간 초과 문제를 해결할 수 있습니다.
"""