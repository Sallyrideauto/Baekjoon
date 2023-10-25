'''
logic
1. 첫 번째 열부터 시작하여 각 행을 기준으로 파이프라인을 설치하는 시도를 합니다.
2. 오른쪽 위, 오른쪽, 오른쪽 아래 순으로 설치 여부를 확인합니다. 이를 위해 DFS 방식으로 탐색합니다.
3. 한 번의 탐색에서 파이프라인 설치에 성공하면 해당 경로를 파이프라인으로 표시하고 다음 행으로 넘어갑니다.
'''
def dfs(r, c):
    # 파이프 설치 성공시 True 반환
    if c == C - 1:
        return True

    # 오른쪽 위, 오른쪽, 오른쪽 아래 순으로 탐색
    directions = [(-1, 1), (0, 1), (1, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and bakery[nr][nc] == '.':
            bakery[nr][nc] = 'x'
            if dfs(nr, nc):
                return True

    return False


R, C = map(int, input().split())
bakery = [list(input()) for _ in range(R)]

count = 0
for i in range(R):
    if dfs(i, 0):
        count += 1

print(count)