import sys

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parents):
    stack = [start]

    while stack:
        node = stack.pop()

        for i in tree[node]:
            if parents[node] != i:
                parents[i] = node
                stack.append(i)

dfs(1, tree, parents)

for i in range(2, n + 1):
    print(parents[i])
    
"""
루트 없는 트리의 경우, 노드간의 관계가 양방향으로 존재합니다. 
따라서 입력으로 주어진 트리 상에서 연결된 두 정점 정보를 바탕으로 
각 노드간의 관계를 파악해야 합니다.
"""