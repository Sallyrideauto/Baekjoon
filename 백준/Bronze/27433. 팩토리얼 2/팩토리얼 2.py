"""
주어진 정수 N에 대한 팩토리얼 N!은 N부터 1까지의 모든 정수를 곱한 값입니다. 
따라서 N!을 구하기 위해서는 1부터 N까지의 모든 정수를 곱하면 됩니다. 
이를 파이썬으로 구현하면 다음과 같습니다.
"""

n = int(input())

factorial = 1
for i in range(1, n+1):
    factorial *= i

print(factorial)

"""
먼저 입력값인 정수 N을 입력받고, 변수 factorial을 1로 초기화합니다. 
그리고 1부터 N까지의 모든 정수를 곱해주기 위해 for문을 이용합니다. 
range(1, n+1)을 이용하여 1부터 N까지의 범위를 반복하고, factorial에 각 숫자를 곱해주면 됩니다. 
마지막으로 print(factorial)을 이용하여 결과값을 출력합니다.
"""