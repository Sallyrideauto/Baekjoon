# https://codechacha.com/ko/python-convert-string-to-list/

def solution(my_string):
    my_str_list = my_string.split(' ')
    answer = []
    
    for elem in my_str_list:
        answer.append(elem)
    
    return answer