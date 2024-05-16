def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        # 스택이 비어있지 않고, 현재 가격이 스택 상단의 가격보다 낮을 때
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    # 스택에 남아 있는 인덱스는 끝까지 가격이 떨어지지 않는 경우 처리
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
        
    return answer