MOD = 1000000000

def count_combinations(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    for i in range(N + 1):
        dp[i][1] = 1

    for i in range(N + 1):
        for j in range(2, K + 1):
            for l in range(i + 1):
                dp[i][j] += dp[l][j - 1]
                dp[i][j] %= MOD
                
    return dp[N][K]

def main():
    N, K = map(int, input().split())
    result = count_combinations(N, K)
    print(result)

if __name__ == "__main__":
    main()

"""
이 프로그램은 동적 계획법을 사용하여 문제를 해결합니다. 
dp[i][j]는 0부터 i까지의 정수 j개를 더해서 그 합이 i가 되는 경우의 수를 저장합니다. 
이를 이용해 주어진 입력에 대해 경우의 수를 계산하고, 결과를 출력합니다.
"""