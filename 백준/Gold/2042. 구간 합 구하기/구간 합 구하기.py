"""
세그먼트 트리는 주어진 구간에 대한 정보를 빠르게 계산하기 위해 사용되는 자료구조입니다. 
여기서는 주어진 수열의 구간 합을 계산하기 위해 사용합니다.

우선 세그먼트 트리의 구조를 간단히 설명하면, 
주어진 수열을 이용하여 완전 이진 트리를 구성한 후, 각 노드는 해당 구간의 합을 저장합니다. 
이를 이용하여 구간 합을 빠르게 계산할 수 있습니다.

세그먼트 트리를 구현하기 위해 먼저 주어진 수열을 이용하여 트리를 초기화합니다. 
그리고 수의 변경이 일어날 때마다 해당 노드의 값을 갱신하고, 
구간 합을 계산할 때는 트리를 순회하면서 해당 구간에 해당하는 노드들의 값을 더해주면 됩니다.

아래는 파이썬으로 구현한 코드입니다. 
시간 복잡도는 O((M+K)logN)입니다.
"""

import sys

def init(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid+1, end, node * 2 + 1)
    return tree[node]

def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node * 2, index, diff)
        update(mid+1, end, node * 2 + 1, index, diff)

def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid+1, end, node * 2 + 1, left, right)

n, m, k = map(int, input().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * (4 * n)

init(0, n-1, 1)

for i in range(m + k):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        index, value = command[1:]
        diff = value - nums[index-1]
        nums[index-1] = value
        update(0, n-1, 1, index-1, diff)
    else:
        left, right = command[1:]
        print(query(0, n-1, 1, left-1, right-1))

"""
sys.stdin.readline()을 사용하여 더 빠르게 입력을 받도록 변경하였습니다. 
또한 range(n)을 range(1, n+1)로 변경하여 인덱스 계산을 간편하게 하였습니다.
"""