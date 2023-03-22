n, m = map(int, input().split())  # 보드의 세로 길이 n, 가로 길이 m을 입력받는다.

board = []  # 보드를 저장할 리스트를 만든다.
for i in range(n):
    board.append(input())

min_cnt = n*m  # 다시 칠해야 하는 정사각형 개수의 최솟값을 저장할 변수를 만들고, 최댓값으로 초기화한다.

for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0  # 맨 왼쪽 위 칸이 흰색인 경우로 시작하는 경우의 다시 칠해야 하는 정사각형 개수
        cnt2 = 0  # 맨 왼쪽 위 칸이 검은색인 경우로 시작하는 경우의 다시 칠해야 하는 정사각형 개수
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l-i-j) % 2 == 0:  # (k, l)이 흰색으로 시작하는 정사각형 안에 있는 경우
                    if board[k][l] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:  # (k, l)이 검은색으로 시작하는 정사각형 안에 있는 경우
                    if board[k][l] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        min_cnt = min(min_cnt, cnt1, cnt2)  # 최솟값을 업데이트한다.

print(min_cnt)
