def solution(arr):
    answer = []
    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer

"""
위 코드에서는 answer라는 빈 리스트를 초기화하고, arr 배열을 순회하면서 각 원소를 확인합니다. 
만약 answer가 비어있거나 현재 확인하고 있는 숫자와 answer의 마지막 원소가 다른 경우에만 해당 숫자를 answer에 추가합니다. 
그렇게 하면 연속적으로 나타나는 숫자는 하나만 남기고 제거할 수 있습니다.

순회가 끝나면 최종적으로 answer 리스트를 반환합니다.
"""