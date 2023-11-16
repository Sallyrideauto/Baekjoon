directions = ['N', 'E', 'S', 'W']
current_direction_index = 0 # 초기 방향은 북쪽(N)

for _ in range(10):
    t = int(input())

    if t == 1:  # 우향우
        current_direction_index = (current_direction_index + 1) % 4
    elif t == 2:    # 뒤로 돌아
        current_direction_index = (current_direction_index + 2) % 4
    elif t == 3:    # 좌향좌
        current_direction_index = (current_direction_index - 1) % 4

print(directions[current_direction_index])