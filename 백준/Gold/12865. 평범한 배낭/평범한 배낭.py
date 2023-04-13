def knapsack(N, K, items):
    dp = [0] * (K + 1)

    for i in range(N):
        w, v = items[i]
        for j in range(K, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[K]

def main():
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    max_value = knapsack(N, K, items)
    print(max_value)

if __name__ == "__main__":
    main()

# 주어진 물건들과 배낭의 무게 한도를 고려하여, 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 계산