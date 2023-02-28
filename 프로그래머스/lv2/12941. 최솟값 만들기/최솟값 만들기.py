def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    
    answer = sum(a * b for a, b in zip(A, B))

    return answer