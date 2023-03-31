n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
sorted_points = sorted(points)
for point in sorted_points:
    print(point[0], point[1])

"""
우선 입력으로 주어진 N을 받은 후, N개의 점을 입력받아 리스트 points에 저장합니다. 
이후 sorted 함수를 이용해 points 리스트를 정렬하면, x좌표를 우선적으로, x좌표가 같은 경우 y좌표를 기준으로 정렬되게 됩니다. 
마지막으로 정렬된 점들을 반복문을 통해 출력합니다.
"""