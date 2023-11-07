import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력 함수를 정의
dq = deque()
output = [] # 출력을 위한 리스트

N = int(input()) # Deque 선언

for _ in range(N):
    command = input().rstrip().split()

    if command[0] == '1':
        dq.appendleft(int(command[1]))
    elif command[0] == '2':
        dq.append(int(command[1]))
    elif command[0] == '3':
        output.append(str(dq.popleft()) if dq else '-1')
    elif command[0] == '4':
        output.append(str(dq.pop()) if dq else '-1')
    elif command[0] == '5':
        output.append(str(len(dq)))
    elif command[0] == '6':
        output.append('1' if not dq else '0')
    elif command[0] == '7':
        output.append(str(dq[0]) if dq else '-1')
    elif command[0] == '8':
        output.append(str(dq[-1]) if dq else '-1')

sys.stdout.write('\n'.join(output))