N, W, H = map(int, input().split())
max_length = (W**2 + H**2)**0.5  # 박스의 대각선 길이
for i in range(N):
    length = int(input())
    if length <= max_length:
        print("DA")
    else:
        print("NE")
