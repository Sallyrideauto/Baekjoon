L = int(input())  # 방학 기간
A = int(input())  # 국어 숙제 페이지 수
B = int(input())  # 수학 숙제 페이지 수
C = int(input())  # 하루에 최대 국어 페이지 수
D = int(input())  # 하루에 최대 수학 페이지 수

# 국어와 수학 숙제를 모두 다 풀 수 있는 기간을 먼저 계산합니다.
korean_days = (A + C - 1) // C  # 올림 연산을 사용하여 국어 숙제를 다 풀기 위해 필요한 날 수 계산
math_days = (B + D - 1) // D  # 올림 연산을 사용하여 수학 숙제를 다 풀기 위해 필요한 날 수 계산
study_days = max(korean_days, math_days)  # 국어와 수학 숙제를 모두 다 풀기 위해 필요한 날 수

# 상근이가 놀 수 있는 최대 날의 수 계산
vacation_days = L - study_days

print(vacation_days)
