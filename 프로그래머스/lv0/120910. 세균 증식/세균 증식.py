def solution(n, t):
    answer = n
    
    for i in range(t):
        answer *= 2
        
    print(answer)
    
    return answer