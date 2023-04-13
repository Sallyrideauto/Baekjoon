def count_ways_to_make_change(coins, n, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        coins = list(map(int, input().split()))
        amount = int(input())

        ways = count_ways_to_make_change(coins, n, amount)
        print(ways)


if __name__ == "__main__":
    main()

"""
이 프로그램은 동전의 종류와 금액이 주어질 때, 
해당 금액을 만드는 모든 방법의 수를 계산합니다. 
동적 프로그래밍을 사용하여 각 금액에 대해 동전의 조합을 저장하고, 
주어진 금액을 만드는 방법의 수를 출력합니다.
"""