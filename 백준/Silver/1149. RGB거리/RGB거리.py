def min_cost_to_paint_houses(N, costs):
    dp = [[0] * 3 for _ in range(N)]

    dp[0] = costs[0]

    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    return min(dp[N - 1])

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
print(min_cost_to_paint_houses(N, costs))

"""
이 프로그램은 집의 수 N과 각 집을 빨강, 초록, 파랑으로 칠하는 비용을 입력받아, 
모든 집을 칠하는 비용의 최솟값을 출력합니다. 
동적 계획법(dynamic programming)을 사용하여 문제를 해결하였습니다.
"""