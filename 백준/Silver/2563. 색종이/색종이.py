# 100x100 크기의 도화지 생성
canvas = [[0] * 100 for _ in range(100)]

# 색종이 수 입력 받기
n = int(input())

# 색종이 위치 입력 받아 검은 영역에 1로 표시
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            canvas[j][k] = 1

# 검은 영역의 넓이 구하기
black_area = 0
for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
            black_area += 1

# 결과 출력
print(black_area)