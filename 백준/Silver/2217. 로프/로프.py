def max_weight(N, ropes):
    # 로프를 내람차순으로 정렬
    ropes.sort(reverse = True)

    # 가능한 최대 중량 계산
    max_w = 0
    for i in range(N):
        # 현재 로프를 포함한 최대 중량 계산
        current_w = ropes[i] * (i + 1)
        # 최대 중량 갱신
        max_w = max(max_w, current_w)

    return max_w

N = int(input())
ropes = [int(input()) for i in range(N)]

print(max_weight(N, ropes))