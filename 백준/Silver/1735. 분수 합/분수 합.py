from math import gcd

def main():
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    # 두 분수의 합 구하기
    numerator_sum = a1 * b2 + a2 * b1
    denominator_sum = b1 * b2

    # 최대공약수 찾기
    greatest_common_divisor = gcd(numerator_sum, denominator_sum)

    # 기약분수로 변환
    reduced_numerator = numerator_sum // greatest_common_divisor
    reduced_denominator = denominator_sum // greatest_common_divisor

    print(reduced_numerator, reduced_denominator)

if __name__ == "__main__":
    main()

"""
이 프로그램은 두 분수를 입력 받아서 합을 구한 다음, 
최대공약수를 찾아 기약분수로 변환하여 출력합니다.
"""