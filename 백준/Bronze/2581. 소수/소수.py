# 아래는 입력받은 M부터 N까지의 모든 자연수 중에서 소수를 찾아 합과 최솟값을 출력하는 파이썬 프로그램입니다.

M = int(input())
N = int(input())

# M부터 N까지의 모든 자연수에 대해 소수인지 판별
primes = []
for num in range(M, N+1):
    if num < 2:
        continue
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            break
    else:
        primes.append(num)

# 소수가 없는 경우
if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))

"""
먼저 입력으로 주어진 M과 N을 변수에 저장합니다. 
그리고 M부터 N까지의 모든 자연수에 대해 소수인지 판별합니다. 
소수 판별은 에라토스테네스의 체를 이용하거나, 
각 숫자마다 2부터 루트n까지의 수로 나누어보는 방법 등 여러 가지 방법이 있습니다. 
이 예시에서는 후자의 방법을 이용합니다.

소수를 찾아낸 후에는 소수의 합과 최솟값을 구합니다. 
소수가 없는 경우에는 -1을 출력합니다.
"""