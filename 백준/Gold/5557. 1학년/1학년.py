def count_expressions(n, numbers):
    dp = [[0] * 21 for _ in range(n)]
    dp[0][numbers[0]] = 1

    for i in range(1, n - 1):
        for j in range(21):
            if dp[i - 1][j] > 0:
                if j + numbers[i] <= 20:
                    dp[i][j + numbers[i]] += dp[i - 1][j]
                if j - numbers[i] >= 0:
                    dp[i][j - numbers[i]] += dp[i - 1][j]

    return dp[n - 2][numbers[-1]]


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    result = count_expressions(n, numbers)
    print(result)


if __name__ == "__main__":
    main()

"""
이 프로그램은 동적 프로그래밍 기법을 사용하여 상근이가 만들 수 있는 올바른 등식의 수를 계산합니다. 
count_expressions 함수에서 각 숫자 위치에서 가능한 모든 수를 기록하며 진행합니다. 
입력된 숫자들을 사용하여 등식의 수를 계산한 후 결과를 출력합니다.
"""