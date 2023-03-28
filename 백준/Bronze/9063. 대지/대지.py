n = int(input()) # 점의 개수 입력
points = [] # 옥구슬 위치를 저장할 리스트

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y)) # 각 점의 위치를 리스트에 저장

# x좌표를 기준으로 오름차순 정렬
points.sort()

# y좌표의 최소값과 최대값을 찾음
min_y = points[0][1]
max_y = points[0][1]
for i in range(1, n):
    if points[i][1] < min_y:
        min_y = points[i][1]
    elif points[i][1] > max_y:
        max_y = points[i][1]

# 대지의 넓이 계산
width = points[-1][0] - points[0][0]
height = max_y - min_y
area = width * height

print(area)

"""
위 프로그램은 입력으로 점의 개수와 각 점의 위치를 받아서 대지의 넓이를 계산합니다.

먼저, 입력으로 받은 각 점의 위치를 리스트 points에 저장합니다. 
그리고 points 리스트를 x좌표를 기준으로 오름차순으로 정렬합니다.

그 다음에는 y좌표의 최소값과 최대값을 찾아서 대지의 높이를 계산합니다. 
이후, 대지의 넓이는 가로 길이와 세로 길이를 곱한 값으로 계산합니다. 
마지막으로, 계산된 대지의 넓이를 출력합니다.
"""