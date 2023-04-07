"""
해당 문제는 DFS나 BFS 알고리즘을 이용하여 해결할 수 있습니다. 
각 배추의 위치를 인접 행렬로 나타내고, 
인접한 배추들끼리는 같은 그룹으로 묶어서 한 마리의 배추흰지렁이로 처리합니다. 
그룹별로 BFS를 수행하면서 처리된 배추를 제외한 다른 배추들을 새로운 그룹으로 묶어서 처리합니다.
"""

from collections import deque

# DFS 함수 정의
def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph[x][y] = 0 # 이미 방문한 배추는 처리함
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)

# BFS 함수 정의
def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 이미 방문한 배추는 처리함
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0 # 이미 방문한 배추는 처리함

# 테스트 케이스 수 입력
t = int(input())

# 각 테스트 케이스에 대해 처리 수행
for _ in range(t):
    # 배추 밭 크기와 배추 위치 수 입력
    m, n, k = map(int, input().split())
    # 배추 밭 그래프 초기화
    graph = [[0] * m for _ in range(n)]
    # 각 배추 위치에 대해 그래프 정보 입력
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1 # 가로축(x)와 세로축(y)을 바꿔 입력함
    # 배추흰지렁이 수 초기화
    count = 0
    # 그래프를 돌며 배추 그룹 수 확인
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    # 배추흰지렁이 수 출력
    print(count)
