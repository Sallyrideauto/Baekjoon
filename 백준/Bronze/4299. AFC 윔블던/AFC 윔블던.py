sum_val, gap_val = map(int, input().split())

# 점수의 합과 차가 모두 짝수여야 하고, 합이 치보다 크거나 같아야 함
if (sum_val + gap_val) % 2 == 0 and sum_val >= gap_val:
    A = (sum_val + gap_val) // 2
    B = sum_val - A
    print(max(A, B), min(A, B)) # 득점이 많은 팀부터 출력
else:
    print(-1)   # 조건을 만족하는 점수가 없는 경우