def solution(t, p):
    p_value = int(p)
    length_p = len(p)
    count = 0
    
    for i in range(len(t) - length_p + 1):
        substring = t[i:i + length_p]
        if int(substring) <= p_value:
            count += 1
            
    return count