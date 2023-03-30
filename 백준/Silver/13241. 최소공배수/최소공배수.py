import math

a, b = map(int, input().split())
lcm = (a * b) // math.gcd(a, b)
print(lcm)

"""
이 코드는 math 모듈에서 제공하는 gcd 함수를 이용하여 입력받은 두 수의 최대공약수를 구한 후, 
두 수의 곱을 최대공약수로 나눈 값을 최소공배수로 저장하여 출력하는 코드입니다. 
변수는 64비트 정수로 선언되어 있습니다.
"""