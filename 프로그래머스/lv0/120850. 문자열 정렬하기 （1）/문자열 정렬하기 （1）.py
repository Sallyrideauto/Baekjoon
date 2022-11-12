import re

def solution(my_string):
    numbers = re.findall(r'\d', my_string)
    answer = [int(i) for i in numbers]
    answer.sort()
    print(answer)
    return answer