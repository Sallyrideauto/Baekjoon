def solution(money):

    answer = []
    
    count = money // 5500
    answer.append(count)
    
    left = money - 5500 * count
    answer.append(left)
    
    return answer