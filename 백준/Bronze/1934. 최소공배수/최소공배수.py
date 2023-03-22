import math

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    lcm = a * b // gcd
    print(lcm)

"""
먼저 입력으로 주어지는 테스트 케이스의 개수를 t 변수에 저장합니다. 
그리고 for 문을 이용해서 t 만큼 반복합니다. 
반복할 때마다 a와 b를 입력받아서, math 모듈의 gcd 함수를 이용해 a와 b의 최대공약수 gcd를 구합니다. 
그리고 a와 b의 곱을 gcd로 나눈 몫을 lcm 변수에 저장하면 a와 b의 최소공배수가 됩니다. 
마지막으로 print 함수를 이용해서 lcm을 출력합니다.
"""