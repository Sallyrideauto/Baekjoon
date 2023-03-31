from collections import deque

# 입력 받기
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 알고리즘 함수 정의
def bfs():
    days = -1  # 최소 일수를 계산하기 위해 days를 -1로 초기화
    while ripe:  # 익은 토마토가 남아있는 동안 반복
        days += 1  # 일수 증가
        for _ in range(len(ripe)):
            x, y = ripe.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    ripe.append((nx, ny))
    for b in box:  # 모든 토마토가 익었는지 확인
        if 0 in b:
            return -1
    return days

# 익은 토마토의 위치를 큐에 저장
ripe = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripe.append((i, j))

# BFS 알고리즘 실행
print(bfs())

"""
위의 코드를 간략히 설명하면, 입력값으로 상자의 크기와 토마토 정보를 받고, 익은 토마토의 위치를 담은 큐를 생성합니다.
그리고 BFS 알고리즘을 이용하여 익은 토마토로부터 인접한 위치의 토마토들을 익게 하면서 최소 일수를 계산합니다.
마지막으로 모든 토마토가 익었는지 확인하고, 익지 않은 토마토가 남아있다면 -1을 출력하고, 모든 토마토가 익었다면 최소 일수를 출력합니다.
"""