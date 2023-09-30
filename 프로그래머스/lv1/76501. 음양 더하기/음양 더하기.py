# https://1ets-just-do-it.tistory.com/39

'''
1차 시도한 코드

def solution(absolutes, signs):
    num = []
    for i in range(len(absolutes)):
        if signs[i] == 'false':
            num.append(-absolutes[i])
        else:
            num.append(absolutes[i])
    return sum(num)
'''

def solution(absolutes, signs):
    result = 0
    for num, sign in zip(absolutes, signs):
        if sign == True:
            result += num
        else:
            result -= num
    return result