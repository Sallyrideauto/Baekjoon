import sys

n = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

# 크레인과 박스를 내림차순으로 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

if max(cranes) < max(boxes):
    # 크레인의 최대 무게보다 가장 무거운 박스가 더 크면 옮길 수 없음
    print(-1)
else:
    # 각 크레인이 옮길 수 있는 박스의 인덱스를 저장하는 리스트
    positions = [0] * n
    # 각 박스의 옮겨진 상태를 나타내는 리스트
    moved = [False] * m
    # 옮기는 시간
    time = 0
    # 옮겨진 박스의 수
    count = 0

    while count < m:
        for i in range(n):
            # 아직 옮겨지지 않은 박스 중에서 옮길 수 있는 가장 무거운 박스를 찾음
            while positions[i] < m:
                if not moved[positions[i]] and cranes[i] >= boxes[positions[i]]:
                    # 해당 박스를 옮길 수 있으면 옮기고 상태를 변경
                    moved[positions[i]] = True
                    count += 1
                    break
                positions[i] += 1

        time += 1

    print(time)