# https://ddolcat.tistory.com/688 참고, 정리할 것

import datetime

def get_days(yyyy, M, D):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[datetime.date(yyyy, M, D).weekday()]

yyyy = 2009
D, M = map(int, input().split())

print(f'{get_days(yyyy, M, D)}')