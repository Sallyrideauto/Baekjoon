from collections import deque

def solve(N, M, positions):
    dq = deque(range(1, N + 1))
    total_rotations = 0
    
    for position in positions:
        # 현재 덱에서 해당 숫자의 위치 찾기
        idx = dq.index(position)
        
        # 왼쪽 회전과 오른쪽 회전 중 최소 회전 결정
        if idx < len(dq) - idx:
            # 왼쪽으로 회전
            dq.rotate(-idx)
            total_rotations += idx
        else:
            # 오른쪽으로 회전
            dq.rotate(len(dq) - idx)
            total_rotations += len(dq) - idx
            
        # 원소 제거
        dq.popleft()
        
    return total_rotations
    
N, M = map(int, input().split())
positions = list(map(int, input().split()))
print(solve(N, M, positions))