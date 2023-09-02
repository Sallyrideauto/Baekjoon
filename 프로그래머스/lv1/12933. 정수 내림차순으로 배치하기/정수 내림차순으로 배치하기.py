def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(i)
        
    answer.sort(reverse = True)
    answer = ''.join(answer)
    answer = int(answer)
    
    return answer