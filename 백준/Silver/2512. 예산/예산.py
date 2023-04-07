n = int(input())  # 지방의 수
requests = list(map(int, input().split()))  # 지방의 예산 요청
m = int(input())  # 총 예산

# 이분 탐색을 위해 요청 금액의 최솟값, 최댓값 설정
start, end = 0, max(requests)

while start <= end:
    mid = (start + end) // 2  # 상한액 계산을 위한 중간값
    total_budget = 0  # 총 예산

    for request in requests:
        if request <= mid:
            total_budget += request  # 상한액 이하인 경우 요청 금액만큼 배정
        else:
            total_budget += mid  # 상한액 이상인 경우 상한액만큼 배정

    if total_budget <= m:  # 총 예산 내에서 배정 가능한 경우
        start = mid + 1  # 상한액을 높여서 배정 가능한 최대 금액을 찾기 위해 start 갱신
        answer = mid  # 현재 상한액을 기록
    else:  # 총 예산 내에서 배정 불가능한 경우
        end = mid - 1  # 상한액을 낮춰서 배정 가능한 최대 금액을 찾기 위해 end 갱신

print(answer)  # 최대 배정 금액 출력

"""
주어진 예산 요청 금액 리스트에서 이분 탐색을 이용해 상한액을 구하고, 
구한 상한액에 따라 총 예산을 계산하여 주어진 총 예산 내에서 최대 배정 금액을 구하는 프로그램입니다.
"""