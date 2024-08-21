def fibonacci_count(max_n):
    # 각 숫자의 호출 횟수를 저장할 배열 초기화
    zero_count = [0] * (max_n + 1)
    one_count = [0] * (max_n + 1)
    
    # 기본 사례
    zero_count[0] = 1
    one_count[1] = 1
    
    # 2 이상의 n에 대해 각각의 호출 횟수 계산
    for i in range(2, max_n + 1):
        zero_count[i] = zero_count[i - 1] + zero_count[i - 2]
        one_count[i] = one_count[i - 1] + one_count[i - 2]
    
    return zero_count, one_count

# 입력받은 N의 최대값에 대해 호출 횟수 미리 계산
max_input = 40  # 문제의 N의 최대 범위
zero_count, one_count = fibonacci_count(max_input)

# 테스트 케이스 입력
t = int(input())
for _ in range(t):
    n = int(input())
    print(zero_count[n], one_count[n])