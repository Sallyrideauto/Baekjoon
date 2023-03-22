# 입력값으로 주어진 n에 해당하는 피보나치 수를 반환하는 파이썬 함수
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
result = fibonacci(n)
print(result)