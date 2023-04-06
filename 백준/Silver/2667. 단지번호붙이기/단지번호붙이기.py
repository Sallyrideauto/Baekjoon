from collections import deque

def bfs(i, j, visited, graph):
    count = 1
    q = deque([(i, j)])
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1

    return count


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
danji_count = 0
danji_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            danji_count += 1
            danji_list.append(bfs(i, j, visited, graph))

print(danji_count)
for cnt in sorted(danji_list):
    print(cnt)
