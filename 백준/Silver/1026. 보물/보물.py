n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# A의 수를 오름차순으로 정렬하고, B의 수를 내림차순으로 정렬
a.sort()
b.sort(reverse=True)

# S의 최솟값 계산
s = sum([a[i]*b[i] for i in range(n)])

print(s)

"""
먼저 입력으로부터 n, a, b를 받습니다. 
리스트 a와 b는 각각 입력에서 주어진 A와 B를 리스트로 만든 것입니다. 
그리고 a의 수를 오름차순으로 정렬하고, b의 수를 내림차순으로 정렬합니다. 
그리고 나서 리스트 컴프리헨션을 이용하여 S의 최솟값을 계산하여 출력합니다.
"""