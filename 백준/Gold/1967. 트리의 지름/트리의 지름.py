"""
먼저 각 노드에 대해서 자식 노드들과 간선 가중치를 저장할 수 있는 자료구조를 만들어야 한다. 
이 문제에서는 dict을 사용하여 {자식 노드: 간선 가중치} 형태로 저장하면 된다. 
이후, DFS를 이용하여 루트 노드부터 가장 먼 노드 u를 찾는다. 
u에서 DFS를 한번 더 진행하여 가장 먼 노드 v를 찾으면, u와 v 사이의 경로가 트리의 지름이 된다. 
이를 구현한 파이썬 프로그램은 아래와 같다.
"""

n = int(input())

# 자식 노드들과 간선 가중치를 저장할 dict
tree = {i: {} for i in range(1, n+1)}

# 입력 받아서 tree dict에 저장
for i in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent][child] = weight
    tree[child][parent] = weight

# DFS 함수. start에서 가장 먼 노드와 그 거리를 반환한다.
def dfs(start):
    visited = [False] * (n+1)
    stack = [(start, 0)] # (현재 노드, 현재 노드까지의 거리) 쌍을 stack에 저장
    max_node, max_dist = start, 0
    while stack:
        node, dist = stack.pop()
        visited[node] = True
        if dist > max_dist:
            max_node, max_dist = node, dist
        for child, weight in tree[node].items():
            if not visited[child]:
                stack.append((child, dist+weight))
    return max_node, max_dist

# 루트 노드에서 가장 먼 노드 u를 찾는다.
u, _ = dfs(1)

# u에서 가장 먼 노드 v를 찾으면, u와 v 사이의 경로가 트리의 지름이 된다.
v, diameter = dfs(u)
print(diameter)