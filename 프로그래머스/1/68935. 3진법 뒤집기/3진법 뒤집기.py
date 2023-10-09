'''
https://1ets-just-do-it.tistory.com/77

def solution(n):
    digits = []
    binary = []
    
    while True:
        if n < 3:
            digits.append(n)
            break
        
        digits.append(n % 3)
        n //= 3
        
    for i in str(digits):
        binary.append(i)
        
    binary = list(map(int, binary))
    num = 0
    
    for i in range(len(binary)):
        num = num * 3 + binary[i]
        
    return num
'''

def solution(n):
    
    result = ''
    
    while n > 0:
        result += str(n % 3)
        n //= 3
        
    return int(result, 3)