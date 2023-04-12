import sys
from math import gcd

def main():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]

    diff = [abs(numbers[i] - numbers[i - 1]) for i in range(1, N)]

    gcd_val = diff[0]
    for d in diff:
        gcd_val = gcd(gcd_val, d)

    divisors = set()
    for i in range(2, int(gcd_val ** 0.5) + 1):
        if gcd_val % i == 0:
            divisors.add(i)
            divisors.add(gcd_val // i)

    divisors.add(gcd_val)
    divisors = sorted(list(divisors))

    print(*divisors)

if __name__ == "__main__":
    main()

"""
이 프로그램은 주어진 N개의 수로부터 가능한 M을 찾기 위해 
먼저 주어진 수들의 차를 구한 후, 그 차들의 최대공약수를 구합니다. 
이 최대공약수의 약수들이 가능한 M 값들입니다. 
마지막으로 약수들을 정렬하여 출력합니다.
"""