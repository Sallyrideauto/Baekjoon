def solution(n):
    answer = []
    
    for i in range(n, 0, -1):
        if n % i == 1:
            answer.append(i)
    
    return min(answer)