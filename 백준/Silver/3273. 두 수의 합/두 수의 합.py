"""
주어진 수열과 자연수 x에 대하여, 
a_i + a_j = x를 만족하는 (a_i, a_j)쌍의 수를 구하는 프로그램
"""

n = int(input())
a = list(map(int, input().split()))
x = int(input())

count = 0
check = set()

for i in range(n):
    if x - a[i] in check:
        count += 1
    check.add(a[i])

print(count)

"""
해당 프로그램은 입력값으로 수열의 크기 n, 수열 a, 자연수 x를 받습니다. 
count 변수를 0으로 초기화하고, check라는 집합(set)을 만듭니다.

수열 a의 각 원소에 대하여, 
x - a[i]가 check 집합에 있으면 count를 1 증가시키고, 
그렇지 않으면 a[i]를 check에 추가합니다.

마지막으로 count를 출력합니다. 
이때, 중복된 쌍을 세지 않도록 주의해야 합니다.
"""