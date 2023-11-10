'''
시간 초과가 발생한 코드

[원인]
1. i not in sold_ticket 구문
   이 연산은 sold_ticket 리스트를 처음부터 끝까지 순회하며 i 값을 찾습니다. 
   이는 매 반복마다 최대 N번의 비교를 필요로 하므로, 전체적으로 O(N^2)의 시간 복잡도를 가집니다.
2. min(ongoing) 구문
   이 연산 역시 ongoing 리스트를 전체 순회하여 최솟값을 찾습니다. 리스트가 커질수록 시간이 많이 소요됩니다.
'''

N = int(input())
sold_ticket = list(map(int, input().split()))
ongoing = []

for i in range(1, max(sold_ticket)):
    if i not in sold_ticket:
        ongoing.append(i)

print(min(ongoing))
