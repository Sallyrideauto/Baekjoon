def escape_students(room_count):
    # 처음에는 모든 방이 잠겨 있음(0: 잠김, 1: 열림)
    rooms = [0] * room_count
    
    for round_num in range(1, room_count + 1):
        for idx in range(round_num - 1, room_count, round_num):
            rooms[idx] = 1 - rooms[idx]    # 방의 상태 변경(잠김 -> 열림, 열림 -> 잠김)
           
    return sum(rooms)    # 열린 방의 수를 반환

T = int(input())    # 테스트 케이스 수

for _ in range(T):
    n = int(input())    # 방의 개수
    print(escape_students(n))