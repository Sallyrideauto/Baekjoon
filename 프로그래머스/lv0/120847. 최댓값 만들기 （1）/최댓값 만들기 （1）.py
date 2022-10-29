def solution(numbers):
    numbers.sort(reverse = True)
    
    a = numbers[0]
    b = numbers[1]
    
    answer = a * b
    print(answer)
    return answer