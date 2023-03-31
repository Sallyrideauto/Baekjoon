def solution(my_string):
    result = ""
    for char in my_string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

"""
위 코드에서는 my_string의 각 문자를 하나씩 검사하여 대문자인 경우 소문자로, 소문자인 경우 대문자로 변환한 후 result 문자열에 추가하고, 최종적으로 result를 반환합니다.
str.islower()와 str.upper()를 사용하여 문자가 소문자인지 확인하고, 대문자로 변환하는 작업을 간단하게 수행할 수 있습니다.
"""