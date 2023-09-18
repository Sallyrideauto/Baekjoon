'''
실패한 코드(정확도 60점 ㄱ-)

def solution(s):

    s = list(s)

    cnt_p, cnt_y = 0

    for i in range(len(s)):
        if s[i] == 'p':
            cnt_p += 1
        if s[i] == 'y':
            cnt_y += 1

    if cnt_p == cnt_y:
        return True
    elif cnt_p == 0 and cnt_y == 0:
        return True

    return False

https://1ets-just-do-it.tistory.com/69
'''

def solution(s):
    s = s.lower()
    
    if s.count('p') == s.count('y'):
        return True
    
    return False