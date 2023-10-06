def solution(price, money, count):
    result = 0
    
    for i in range(1, count + 1):
        result += (price * i)
    
    if money >= result:
        return 0
    else:
        result -= money
        return result