"""
이 문제는 벽을 세울 수 있는 경우의 수를 모두 구하고, 
각 경우에서 안전 영역의 크기를 구하여 최댓값을 찾는 문제입니다. 
벽을 세울 수 있는 경우의 수는 DFS나 BFS를 이용하여 구할 수 있습니다.

우선 입력을 받고, 벽을 세울 수 있는 모든 경우의 수를 구합니다. 
이 때, DFS를 이용하여 벽을 3개 세울 위치를 정합니다. 
벽을 세운 후, BFS를 이용하여 바이러스가 퍼져나가는 지도를 만들어 줍니다. 
안전 영역의 크기는 빈 칸의 수에서 바이러스가 퍼진 칸의 수를 뺀 것이므로, 
이 값을 구해 최댓값을 찾습니다.
"""

from collections import deque
import copy

N, M = map(int, input().split())
graph = []
empty = []  # 빈 칸의 좌표
virus = []  # 바이러스의 좌표

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(M):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))

def bfs(graph):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

def get_safety_area(graph):
    bfs(graph)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

# 벽을 세울 수 있는 모든 경우의 수를 구합니다.
walls = []
for i in range(len(empty)):
    for j in range(i + 1, len(empty)):
        for k in range(j + 1, len(empty)):
            walls.append([empty[i], empty[j], empty[k]])

# 최대 안전 영역 크기를 구합니다.
answer = 0
for w in walls:
    g = copy.deepcopy(graph)
    g[w[0][0]][w[0][1]] = 1
    g[w[1][0]][w[1][1]] = 1
    g[w[2][0]][w[2][1]] = 1
    area = get_safety_area(g)
    answer = max(answer, area)

print(answer)
