def solution(arr):
    answer = []
    
    for elem in arr:
        if elem >= 50 and elem % 2 == 0:
            answer.append(elem // 2)
        elif elem <= 50 and elem % 2 == 1:
            answer.append(elem * 2)
        else:
            answer.append(elem)
            
    return answer