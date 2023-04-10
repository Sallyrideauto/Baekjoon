import math

def find_square_numbers(m, n):
    square_numbers = []
    for i in range(m, n + 1):
        sqrt_i = int(math.sqrt(i))
        if sqrt_i * sqrt_i == i:
            square_numbers.append(i)
    return square_numbers

def main():
    M = int(input())
    N = int(input())

    square_numbers = find_square_numbers(M, N)

    if len(square_numbers) > 0:
        print(sum(square_numbers))
        print(min(square_numbers))
    else:
        print(-1)

if __name__ == "__main__":
    main()

"""
이 프로그램은 먼저 find_square_numbers 함수를 사용하여 M과 N 사이의 완전 제곱수를 찾은 후, 찾은 제곱수들의 합과 최솟값을 출력합니다.
만약 M과 N 사이에 완전 제곱수가 없다면 -1을 출력합니다.
"""