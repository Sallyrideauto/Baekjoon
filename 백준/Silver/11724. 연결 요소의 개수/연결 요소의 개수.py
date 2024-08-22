import sys
sys.setrecursionlimit(10000)  # 재귀 한도 증가

def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)

input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
component_count = 0

for index in range(2, len(data), 2):
    u = int(data[index])
    v = int(data[index + 1])
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        component_count += 1

print(component_count)