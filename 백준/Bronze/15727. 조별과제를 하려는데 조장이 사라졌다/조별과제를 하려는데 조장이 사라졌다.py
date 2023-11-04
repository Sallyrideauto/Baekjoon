'''
이 문제를 해결하기 위해 우리는 최대 속도로 성우가 민건이의 집에 도착할 수 있는 최소 시간을 계산해야 합니다.
성우가 1분에 1에서 5까지의 거리를 이동할 수 있다면,
이 문제는 성우가 매 분마다 최대 거리를 이동한다고 가정할 때 걸리는 시간을 계산하는 것으로 단순화될 수 있습니다.

이 경우, 성우가 이동할 수 있는 최대 거리는 5이므로 거리 ( L )을 5로 나눈 값을 올림하면 됩니다.
이는 성우가 1분에 최대 5의 거리를 이동할 수 있으므로, ( L )을 5로 나누어 성우가 필요한 최소 분을 계산할 수 있음을 의미합니다.
파이썬에서 올림을 계산하려면 math.ceil 함수를 사용합니다.
'''

import math
def find_minho(distance):
    '''
    성우가 민건이의 집까지 걸리는 최고 시간을 계산하는 함수

    :param distance: 성우의 현재 위치에서 민건이의 집까지의 거리 L
    :return: 최소 시간 t
    '''

    # 성우가 1분에 이동할 수 있는 최대 거리는 5이므로, 거리를 5로 나눈 값을 올림
    return math.ceil(distance / 5)

L = int(input())

# 성우가 민건이를 찾는 데 필요한 최소 시간 계산
min_minutes = find_minho(L)

print(min_minutes)