def solution(arr, divisor):
    answer = []
    
    for elem in arr:
        if elem % divisor == 0:
            answer.append(elem)
            
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()
    
    return answer