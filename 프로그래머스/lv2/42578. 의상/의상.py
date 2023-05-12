from collections import defaultdict

def solution(clothes):
    # 의상의 종류별로 개수를 저장할 딕셔너리 생성
    count = defaultdict(int)

    # 의상의 종류별로 개수 카운트
    for _, category in clothes:
        count[category] += 1

    # 각 의상 종류별로 선택할지 안 할지의 경우의 수에 1을 더해 곱해줌
    answer = 1
    for num in count.values():
        answer *= (num + 1)

    # 아무 의상도 선택하지 않은 경우를 제외하고 반환
    return answer - 1

"""
위 코드에서는 defaultdict를 사용하여 의상의 종류별로 개수를 카운트합니다. 
그리고 각 의상 종류별로 선택할지 안 할지의 경우의 수를 계산하기 위해 1을 더하고 곱해줍니다. 
마지막으로 아무 의상도 선택하지 않은 경우를 제외하기 위해 1을 빼고 결과를 반환합니다.
"""