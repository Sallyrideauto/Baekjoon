from collections import deque
import sys

N = int(sys.stdin.readline())
deq = deque()

for i in range(N):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push_front':
        deq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    elif cmd[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        print(0 if deq else 1)
    elif cmd[0] == 'front':
        print(deq[0] if deq else -1)
    elif cmd[0] == 'back':
        print(deq[-1] if deq else -1)

        
"""
입력으로 주어지는 명령을 처리하는 프로그램입니다. 
덱은 파이썬 collections 모듈의 deque를 사용했습니다. 
명령어에 따라 deque의 앞이나 뒤에 정수를 삽입하거나 삭제하면서, 출력할 결과를 조건에 따라 출력합니다. 
여기서 입력 함수로 stdin을 사용하여 입력 속도를 높였습니다.
"""