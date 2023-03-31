from collections import deque

# DFS 함수 정의
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

# BFS 함수 정의
def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(1, n+1):
            if not visited[i] and graph[node][i] == 1:
                queue.append(i)
                visited[i] = True

# 정점의 개수 n, 간선의 개수 m, 탐색을 시작할 정점의 번호 v 입력받기
n, m, v = map(int, input().split())

# 그래프 초기화
graph = [[0] * (n+1) for _ in range(n+1)]

# 간선 정보 입력받아 그래프에 반영
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# DFS 수행
visited = [False] * (n+1)
dfs(v)
print()

# BFS 수행
visited = [False] * (n+1)
bfs(v)
print()

"""
위 프로그램에서는 DFS 함수와 BFS 함수를 각각 정의하여 그래프를 탐색합니다. 

우선 입력으로 받은 정점의 개수, 간선의 개수, 시작 정점 번호를 이용하여 그래프를 초기화합니다. 
그 다음 간선 정보를 입력받아 그래프에 반영합니다. 
이후 DFS 함수와 BFS 함수를 각각 호출하여 그래프를 탐색합니다. 

방문 여부를 나타내는 visited 배열을 이용하여 이미 방문한 정점은 다시 방문하지 않도록 처리합니다. 
DFS 함수에서는 현재 정점을 출력하고 방문하지 않은 인접한 정점 중에서 번호가 작은 정점부터 방문합니다. 
BFS 함수에서는 큐를 이용하여 현재 정점과 인접한 정점들을 순서대로 방문합니다. 

모든 정점을 방문할 때까지 탐색을 수행한 뒤 방문한 정점들을 출력합니다.
"""