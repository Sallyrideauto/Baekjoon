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

"""
코드는 지도를 입력받은 후에 DFS(깊이 우선 탐색) 알고리즘을 이용하여 단지를 찾는 것입니다.

우선, 입력받은 지도를 2차원 배열로 저장합니다. 
그리고 각 좌표를 방문했는지 체크하기 위한 visited 배열도 만듭니다.

그 후, 각 좌표에 대해서 DFS를 수행하면서 연결된 집들을 모두 찾아냅니다. 
이때, 현재 좌표와 연결된 집이 있는 좌표는 상, 하, 좌, 우 4개 방향에 있는 좌표들입니다. 
이를 모두 방문하면서, 방문하지 않은 집이 있는 경우 해당 집도 DFS를 수행하여 연결된 모든 집을 찾습니다.

DFS를 수행할 때마다, 해당 단지에 속한 집의 수를 1씩 증가시키고, visited 배열에도 방문 체크를 합니다.

모든 좌표에 대해서 DFS를 수행하면, 단지 수와 각 단지에 속한 집의 수를 출력하면 됩니다. 
이때, 각 단지에 속한 집의 수는 리스트에 저장한 뒤에 오름차순으로 정렬하여 출력합니다.
"""
