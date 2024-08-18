def solution(n):
    numbers = [x for x in range(n + 1)]
        
    is_prime = [True] * 1000001   # 0 ~ 1000001까지의 수를 모두 소수(True)로 초기화
    is_prime[0], is_prime[1] = False, False # 0과 1은 소수가 아니므로 False
    
    for i in range(2, 1000001):   # 2부터 n까지 반복
        if is_prime[i]: # 소수일 경우
            for j in range(i * 2, 1000001, i):    # 소수의 배수는 모두 소수가 아니므로 False
                is_prime[j] = False

    ans_cnt = 0

    for num in numbers:
        if is_prime[num]:
            ans_cnt += 1
            
    return ans_cnt