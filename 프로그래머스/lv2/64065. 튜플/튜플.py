"""
문자열 s에 주어진 튜플을 배열에 담아 반환하는 문제입니다. 
주어진 튜플을 파싱하여 숫자들을 추출하고, 
숫자의 빈도를 기준으로 배열에 담는 방식으로 문제를 해결할 수 있습니다.

1. s 문자열에서 필요한 숫자들을 추출합니다. 
   숫자는 쉼표(,)로 구분되어 있으므로 쉼표를 기준으로 문자열을 나누고, 
   각 숫자를 정수로 변환하여 리스트에 저장합니다.
2. 숫자들의 빈도를 계산하여 딕셔너리에 저장합니다.
3. 딕셔너리를 빈도를 기준으로 내림차순 정렬합니다.
4. 정렬된 숫자들을 순서대로 배열에 담아 반환합니다.
"""

def solution(s):
    numbers = s[2:-2].split("},{")  # 숫자들 추출
    numbers = [list(map(int, num.split(","))) for num in numbers]  # 숫자들 리스트로 변환

    freq_dict = {}
    for num_list in numbers:
        for num in num_list:
            freq_dict[num] = freq_dict.get(num, 0) + 1  # 빈도 계산

    sorted_nums = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)  # 빈도 기준으로 정렬

    answer = []
    for num in sorted_nums:
        answer.append(num)

    return answer
