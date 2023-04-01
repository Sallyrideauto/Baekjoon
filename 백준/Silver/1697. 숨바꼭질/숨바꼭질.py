from collections import deque

n, k = map(int, input().split())

# visited 리스트를 생성하여 방문한 적 있는 위치를 기록합니다.
visited = [False] * 100001

# BFS 탐색을 위해 큐를 생성합니다.
queue = deque([(n, 0)])

while queue:
    x, time = queue.popleft()

    # 수빈이가 동생을 찾으면 걸린 시간을 출력하고 프로그램을 종료합니다.
    if x == k:
        print(time)
        break

    # 걷는 경우에 대한 탐색
    for nx in (x-1, x+1):
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            queue.append((nx, time+1))

    # 순간이동하는 경우에 대한 탐색
    nx = x*2
    if 0 <= nx <= 100000 and not visited[nx]:
        visited[nx] = True
        queue.append((nx, time+1))

"""
이 코드에서는 BFS 탐색을 사용하여 수빈이가 동생을 찾는 가장 빠른 시간을 계산합니다. 
큐에는 현재 위치와 걸린 시간을 저장하고, 반복문을 돌면서 걷거나 순간이동할 때의 경우에 대해 탐색합니다. 
이 때, 방문한 적 있는 위치는 visited 리스트에 True로 표시하여 중복 탐색을 방지합니다. 
수빈이가 동생을 찾으면 걸린 시간을 출력하고 반복문을 종료합니다.
"""