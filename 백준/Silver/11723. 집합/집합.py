import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in s else 0)
    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        if x in s:
            s.discard(x)
        else:
            s.add(x)
    elif cmd[0] == 'all':
        s = set(range(1, 21))
    elif cmd[0] == 'empty':
        s.clear()

"""
위 코드에서 set은 중복을 허용하지 않는 특징을 가지고 있으며, add와 discard 메소드를 이용하여 값을 추가하거나 삭제할 수 있습니다.
check 연산은 in 연산을 이용한 리스트 검색 대신 in 연산을 이용한 set 검색으로 구현하였습니다.
all 연산은 range 함수와 set 생성자를 이용하여 1부터 20까지의 값을 가지는 set으로 초기화합니다.
empty 연산은 clear 메소드를 이용하여 set을 초기화합니다.
이렇게 구현하면 시간 복잡도가 O(M)으로 제한된 입력 크기에서도 빠르게 실행됩니다.
"""