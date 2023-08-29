def solution(n, numlist):
    answer = []
    
    for elem in numlist:
        if elem % n == 0:
            answer.append(elem)
    
    return answer