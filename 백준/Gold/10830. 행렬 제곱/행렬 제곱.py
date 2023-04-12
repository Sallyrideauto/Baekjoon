import sys
from functools import reduce

MOD = 1000

def multiply_matrices(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD

    return result

def matrix_power(A, B):
    n = len(A)
    if B == 1:
        return [[A[i][j] % MOD for j in range(n)] for i in range(n)]

    if B % 2 == 0:
        half = matrix_power(A, B // 2)
        return multiply_matrices(half, half)
    else:
        return multiply_matrices(A, matrix_power(A, B - 1))

def main():
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    result = matrix_power(A, B)

    for row in result:
        print(*row)

if __name__ == "__main__":
    main()

"""
이 프로그램은 행렬 곱셈과 분할 정복 기법을 사용하여 문제를 해결합니다. 
행렬 A를 B제곱하는 것은 A를 B-1제곱한 행렬과 A를 곱하는 것과 동일합니다. 
이를 반복적으로 분할하며 계산하여 최종 결과를 출력합니다. 
각 원소를 1,000으로 나눈 나머지를 구하기 위해 모듈러 연산을 사용합니다.
"""