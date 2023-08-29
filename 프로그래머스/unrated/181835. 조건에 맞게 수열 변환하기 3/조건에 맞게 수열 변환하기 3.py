def solution(arr, k):
    
    result = []
    
    if k % 2 == 1:
        for elem in arr:
            result.append(elem * k)
    else:
        for elem in arr:
            result.append(elem + k)
            
    return result