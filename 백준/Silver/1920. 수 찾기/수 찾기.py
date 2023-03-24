# 입력받은 정수 배열을 집합(set)으로 변환한 후, 
# M개의 수들 중에 집합에 존재하는지 확인하는 코드

N = int(input())
A = set(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in A:
        print(1)
    else:
        print(0)
