def max_sum_with_removal(n, numbers):
    dp = [0] * n
    dp2 = [0] * n

    dp[0] = numbers[0]
    dp2[n - 1] = numbers[n - 1]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + numbers[i], numbers[i])

    for i in range(n - 2, -1, -1):
        dp2[i] = max(dp2[i + 1] + numbers[i], numbers[i])

    max_sum = max(dp)

    for i in range(1, n - 1):
        max_sum = max(max_sum, dp[i - 1] + dp2[i + 1])

    return max_sum


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    result = max_sum_with_removal(n, numbers)
    print(result)


if __name__ == "__main__":
    main()

    
"""
이 프로그램은 동적 프로그래밍을 사용하여 주어진 수열에서 수를 제거하지 않거나 하나 제거할 수 있는 경우에 가장 큰 합을 계산합니다. 
max_sum_with_removal 함수에서 두 개의 동적 프로그래밍 테이블을 사용하여 각 위치에서의 최대 합을 계산한 후, 최대 합을 반환합니다. 
입력된 수열을 사용하여 최대 합을 계산한 후 결과를 출력합니다.
"""