# 주어진 배열 citations를 정렬한 뒤, 각 인용 횟수별로 H-Index를 계산하는 방법을 사용하여 문제를 해결

def solution(citations):
    n = len(citations)
    citations.sort()  # 인용 횟수를 오름차순으로 정렬

    h_index = 0
    for i in range(n):
        if citations[i] >= n - i:
            h_index = n - i
            break

    return h_index

"""
위의 코드는 citations를 오름차순으로 정렬한 후, 각 인용 횟수에 대해 H-Index를 계산합니다. 
인용 횟수가 현재 위치의 논문 수 이상인 경우, 해당 인용 횟수를 H-Index로 갱신하고 반복문을 종료합니다.
"""