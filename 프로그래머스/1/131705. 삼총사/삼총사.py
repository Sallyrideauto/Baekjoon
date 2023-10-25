'''
[문제 해결 로직]
1. 주어진 number 배열에서 3개의 숫자를 선택합니다.
2. 선택된 3개의 숫자의 합이 0인지 확인합니다.
3. 합이 0인 경우에 카운트를 증가시킵니다.
4. 모든 가능한 3개의 숫자의 조합을 확인한 후, 카운트 값을 반환합니다.
'''

from itertools import combinations

def solution(number):
    # 세 숫자의 조합에서 합이 0인 경우를 카운트
    count = 0
    for comb in combinations(number, 3):    # number에서 3개의 숫자를 선택하는 모든 조합
        if sum(comb) == 0:  # 선택된 3개의 숫자의 합이 0인 경우
            count += 1
    return count