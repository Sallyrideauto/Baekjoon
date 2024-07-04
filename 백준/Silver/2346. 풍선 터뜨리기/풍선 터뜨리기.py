from collections import deque

def solve_balloons(n, balloons):
    dq = deque((i, x) for i, x in enumerate(balloons, 1))   # (풍선 번호, 풍선 안의 숫자)
    result = []
    
    while dq:
        idx, num = dq.popleft() # 현재 터뜨릴 풍선
        result.append(idx)  # 터뜨린 풍선의 번호 저장
        
        if not dq:
            break
        
        if num > 0:
            num -= 1    # 현재 위치 제외하고 오른쪽으로 이동
            
        dq.rotate(-num) # 음수면 왼쪽, 양수면 오른쪽으로 회전
        
    return result
    
# 입력 받기
n = int(input())
balloons = list(map(int, input().split()))  # 각 풍선 안의 숫자

# 결과 출력
result = solve_balloons(n, balloons)
print(' '.join(map(str, result)))