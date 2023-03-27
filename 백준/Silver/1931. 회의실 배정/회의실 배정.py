n = int(input())
meetings = []

# 입력받은 회의 정보를 meetings 리스트에 저장
for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간이 빠른 순서대로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 가장 빨리 끝나는 회의 선택
last_end_time = 0
count = 0
for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)

"""
위 코드는 입력으로 회의의 개수 n과 각 회의의 시작 시간과 끝나는 시간을 받아 meetings 리스트에 저장합니다. 
그리고 meetings 리스트를 끝나는 시간이 빠른 순서대로 정렬합니다. 
이후 last_end_time 변수를 이용하여 이전에 배정한 회의의 끝나는 시간과 현재 회의의 시작 시간을 비교하며, 회의를 배정할 수 있는지 여부를 판단합니다. 
만약 현재 회의의 시작 시간이 이전에 배정한 회의의 끝나는 시간보다 크거나 같다면 해당 회의를 배정하고, last_end_time 변수를 현재 회의의 끝나는 시간으로 업데이트합니다. 
이 과정을 반복하여 최대한 많은 회의를 배정한 후, 배정된 회의의 개수를 출력합니다.
"""