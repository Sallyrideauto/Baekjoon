def solution(slice, n):
    answer = 0
    
    a = n / slice
    b = n % slice
    
    if b == 0:
        answer = a * 1
    else:
        answer = a * 1 + 1
        
    answer = int(answer)
    print(answer)
    
    return answer