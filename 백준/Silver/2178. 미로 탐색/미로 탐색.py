# 참고한 사이트
# https://jobdong7757.tistory.com/93
# https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html
# https://ooyoung.tistory.com/117

from collections import deque 

n, m = map(int, input().split()) 
graph=[] 

for i in range(n): 
    graph.append(list(map(int, input()))) 
    
def bfs(a, b): 
    q = deque() 
    q.append((a, b)) 
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, 1, -1] 
    while q: 
        x, y = q.popleft() 
        for i in range(4): 
            nx = x + dx[i] 
            ny = y + dy[i] 
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1: 
                q.append((nx, ny)) 
                graph[nx][ny] = graph[x][y] + 1 

bfs(0, 0)
print(graph[n-1][m-1])
