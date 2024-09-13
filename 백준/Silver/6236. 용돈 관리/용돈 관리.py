def can_withdraw_with_limit(limit, M, expenses):
    count = 1  # 첫 번째 인출
    current_sum = 0
    
    for expense in expenses:
        if current_sum + expense > limit:
            count += 1  # 새로운 인출
            current_sum = expense
            if count > M:  # 인출 횟수가 M을 초과하면 실패
                return False
        else:
            current_sum += expense
            
    return True

def find_minimum_withdraw(N, M, expenses):
    left = max(expenses)  # 인출 금액의 최소값 (최소 하루 지출)
    right = sum(expenses)  # 인출 금액의 최대값 (모든 지출의 합)
    
    result = right  # 최종 최소 금액을 저장할 변수
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_withdraw_with_limit(mid, M, expenses):
            result = mid  # 가능한 경우 mid 값을 저장
            right = mid - 1  # 더 작은 값이 가능한지 확인
        else:
            left = mid + 1  # 더 큰 인출 금액이 필요
            
    return result

# 입력 받기
N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]

# 결과 출력
print(find_minimum_withdraw(N, M, expenses))
