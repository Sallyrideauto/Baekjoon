# 에라토스테네스의 체 알고리즘을 사용하여 소수를 찾아내는 파이썬 코드

n = int(input()) # 수의 개수 입력받기
numbers = list(map(int, input().split())) # 수 입력받기

is_prime = [True] * 1001 # 0 ~ 1000까지의 수를 모두 소수(True)로 초기화
is_prime[0], is_prime[1] = False, False # 0과 1은 소수가 아니므로 False로 변경

for i in range(2, 1001): # 2부터 1000까지 반복
    if is_prime[i]: # 소수일 경우
        for j in range(i*2, 1001, i): # 소수의 배수는 모두 소수가 아니므로 False로 변경
            is_prime[j] = False

count = 0 # 소수의 개수를 저장할 변수 초기화
for num in numbers:
    if is_prime[num]: # 소수일 경우
        count += 1

print(count) # 소수의 개수 출력

"""
위 코드에서는 입력된 수 중에서 1000 이하의 모든 소수를 찾아내고, 
입력된 수가 소수인지 아닌지를 확인하여 소수의 개수를 구합니다.
"""