def solution(array, height):
    answer = []
    
    for i in range (len(array)):
        if array[i] > height:
            answer.append(array[i])
            
    answer = len(answer)
    print(answer)
    
    return answer