def solution(n):
    answer = []
    
    for i in range(1, n):
        if i % 2 == 1:
            answer.append(i)
    if n % 2 == 1:
        answer.append(n)
    
    print(answer)
    
    return answer