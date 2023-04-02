t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    f = 2 - v + e
    print(f)

"""
각 테스트 케이스마다 꼭짓점의 수와 모서리의 수를 입력받고, 
이를 이용하여 면의 수를 계산하여 출력합니다.
"""