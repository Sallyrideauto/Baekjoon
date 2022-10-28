def solution(num_list):
    
    even = 0
    odd = 0
    
    answer = []
    
    for i in num_list:
        if i % 2 == 0:
            even += 1
            answer.append(even)
        else:
            odd += 1
            answer.append(odd)

    return even, odd
    
    return answer