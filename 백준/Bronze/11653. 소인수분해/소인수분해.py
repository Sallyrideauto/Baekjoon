def prime_factorization(n):
    i = 2
    while n > 1:
        while n % i == 0:
            print(i)
            n //= i
        i += 1

def main():
    N = int(input())
    prime_factorization(N)

if __name__ == "__main__":
    main()

"""
이 프로그램은 prime_factorization 함수를 사용하여 주어진 정수 N을 소인수분해합니다.
소인수분해 결과는 한 줄에 하나씩 오름차순으로 출력됩니다.
N이 1인 경우 아무것도 출력하지 않습니다.
"""