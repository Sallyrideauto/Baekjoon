def solution(s):
    answer = []
    
    for c in s:
        if c == '(':
            answer.append(c)
        elif c == ')':
            if not answer:
                return False
            answer.pop()
    return not answer