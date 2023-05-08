def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n, k = map(int, input().split())
print(binomial_coefficient(n, k))

"""
위 코드는 먼저 팩토리얼을 계산하는 함수 factorial을 정의한 후, 
이를 이용해 이항 계수를 계산하는 함수 binomial_coefficient를 정의합니다. 
마지막으로 입력을 받아 이항 계수를 계산하고 출력합니다.
"""