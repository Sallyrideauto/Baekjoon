# 소수 판별을 빠르게 사용 가능한 O(route n) 알고리즘
# n개의 수를 O(route n)의 시간 복잡도로 소수를 판별하므로 총 시간 복잡도는 O(route n * n)

# 소수 판별을 위한 prime_check 함수 정의
def prime_check(num):
    # 수가 1일 경우 소수가 아니므로 False를 반환
    if num == 1:
        return False
    # 그렇지 않을 경우 2부터 route n까지의 수를 탐색하기 위해 for문 사용
    else:
        for i in range(2, int(num ** 0.5) + 1):
            # 해당 수가 i로 나누어 떨어진다면 소수가 아니므로 False 반환
            if num % i == 0:
                return False
        return True     # 나누어 떨어지지 않는다면 소수이므로 True 반환

M, N = map(int, input().split())

for i in range(M, N + 1):
    # 해당하는 수가 소수인지 판별하기 위해 코드라인 1의 prime_check 함수를 실행하며, 소수라면 그 수를 출력
    if prime_check(i):
        print(i)