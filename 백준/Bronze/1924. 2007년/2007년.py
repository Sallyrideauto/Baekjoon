# https://ddolcat.tistory.com/688 참고, 정리할 것

import datetime

def get_days(yyyy, mm, dd):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return days[datetime.date(yyyy, mm, dd).weekday()]

yyyy = 2007
mm, dd = map(int, input().split())

print(f'{get_days(yyyy, mm, dd)}')
