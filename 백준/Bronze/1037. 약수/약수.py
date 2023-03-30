"""
주어진 진짜 약수들을 이용하여 원래의 수를 구하는 방법은, 
진짜 약수들을 오름차순으로 정렬한 후, 첫 번째 약수와 마지막 약수의 곱을 구하면 된다. 
이는 모든 진짜 약수가 주어졌기 때문에 가능한 방법이다.
"""

n = int(input())
divisors = sorted(list(map(int, input().split())))

# 첫 번째 약수와 마지막 약수를 곱한다.
result = divisors[0] * divisors[-1]

print(result)
