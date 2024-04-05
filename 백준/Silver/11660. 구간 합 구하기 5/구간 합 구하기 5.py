import sys

n, m = map(int, sys.stdin.readline().split())

table = [[0] * (n + 1) for _ in range(n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    table[i] = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + table[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])

'''
표의 크기 N과 합을 구해야 하는 횟수 M을 입력받는다.
표의 크기 N만큼 표를 입력받는다.
표를 입력받을 때, 각 행의 맨 앞에 0을 추가한다.

dp 테이블을 만들어준다.
dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + table[i][j]
dp[i][j] = (1, 1)부터 (i, j)까지의 합을 의미한다.
'''