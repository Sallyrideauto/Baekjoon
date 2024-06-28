def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    # 방문한 노드 수를 세기 위해 전역 변수 사용
    global count
    count += 1
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
            
n = int(input())    # 컴퓨터의 수
m = int(input())    # 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)]  # 각 노드에 연결된 노드 정보를 담는 리스트
visited = [False] * (n + 1) # 방문한 노드 체크
count = 0   # 바이러스에 감염된 컴퓨터의 수

# 모든 연결 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 1번 컴퓨터에서 시작하여 DFS 수행
dfs(graph, 1, visited)

# 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력
print(count - 1)