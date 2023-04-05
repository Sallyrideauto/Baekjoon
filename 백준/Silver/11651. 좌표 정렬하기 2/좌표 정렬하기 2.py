n = int(input()) # 점의 개수 입력받기
points = [] # 점들을 저장할 리스트

# n개의 점을 입력받아 points 리스트에 저장하기
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y)) # x, y를 튜플로 묶어서 저장

# 정렬하기
points.sort(key=lambda point: (point[1], point[0])) # y좌표 오름차순, y좌표 같으면 x좌표 오름차순으로 정렬

# 결과 출력하기
for point in points:
    print(point[0], point[1])
