"""
다익스트라(Dijkstra) 알고리즘을 사용하여 최단 경로를 구할 수 있습니다.
우선순위 큐를 사용하여 최소 거리를 유지하며 탐색합니다.
"""

import heapq
import sys

# 입력 받기
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
INF = 1e9
distance = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 결과 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

"""
입력으로부터 시작 정점, 그래프 정보를 받고, dijkstra 함수를 호출하여 최단 거리를 계산합니다. 
결과를 출력할 때, INF 값을 가지는 경우는 경로가 존재하지 않는 경우이므로 "INF"를 출력하고, 
그렇지 않은 경우에는 최단 거리 값을 출력합니다.
"""