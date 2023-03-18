x, y, w, h = map(int, input().split())

# 직사각형의 가장자리까지의 거리 계산
left_distance = x
right_distance = w - x
bottom_distance = y
top_distance = h - y

# 최소 거리 계산
min_distance = min(left_distance, right_distance, bottom_distance, top_distance)

print(min_distance)
