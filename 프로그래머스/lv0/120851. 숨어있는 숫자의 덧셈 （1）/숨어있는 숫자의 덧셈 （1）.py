# https://codechacha.com/ko/python-sum/
# https://shayete.tistory.com/entry/%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84-int-%ED%98%95%ED%83%9C%EB%A1%9C-%EB%B3%80%ED%99%98

import re

def solution(my_string):
    numbers = re.findall(r'\d', my_string)
    numbers = [int(i) for i in numbers]
    
    answer = sum(numbers)
    
    print(answer)
    
    return answer