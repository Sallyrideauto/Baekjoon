def solve():
    N = int(input())    # 발전소의 수
    cost = [list(map(int, input().split())) for _ in range(N)]    # 각 발전소의 비용
    
    initial_state = input()    # 현재 발전소 상태
    P = int(input())    # 목표로 하는 최소 가동 발전소 수
    
    # 현재 상태를 비트마스크로 전환
    current_mask = 0
    count_on = 0
    for i, state in enumerate(initial_state):
        if state == 'Y':
            current_mask |= (1 << i)
            count_on += 1
            
    if count_on >= P:
        return 0    # 이미 목표를 달성한 경우
    
    # DP 배열 초기화
    INF = float('inf')
    dp = [INF] * (1 << N)
    dp[current_mask] = 0
    
    # DP를 통한 최소 비용 계산
    for mask in range(1 << N):
        if dp[mask] == INF:
            continue
        for i in range(N):
            if mask & (1 << i):    # i가 켜져 있는 경우
                for j in range(N):
                    if not (mask & (1 << j)):
                        new_mask = mask | (1 << j)
                        dp[new_mask] = min(dp[new_mask], dp[mask] + cost[i][j])
                        
    # 최소 비용 찾기
    result = INF
    for mask in range(1 << N):
        if bin(mask).count('1') >= P:
            result = min(result, dp[mask])
            
    return result if result != INF else -1

if __name__ == "__main__":
    print(solve())