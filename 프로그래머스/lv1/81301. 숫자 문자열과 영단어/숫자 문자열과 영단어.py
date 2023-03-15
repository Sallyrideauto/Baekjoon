def solution(s):
    # 각 숫자에 대응되는 영단어를 키-값 쌍으로 딕셔너리에 저장
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # 숫자에 대응되는 영단어를 숫자로 변환하여 리턴
    for key, value in num_dict.items():
        s = s.replace(key, value)

    return int(s)