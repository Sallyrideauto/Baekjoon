import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0  # 스택의 크기를 저장할 변수 추가

    def push(self, item):
        self.stack.append(item)
        self.count += 1 # 스택에 원소를 추가할 때마다 크기를 1 증가

    def pop(self):
        if self.count > 0:
            self.count -= 1  # 스택에서 원소를 빼낼 때마다 크기를 1 감소
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def top(self):
        if self.count > 0:
            return self.stack[-1]
        else:
            return -1

input = sys.stdin.readline
stack = Stack()
result = [] # 출력 결과를 저장할 리스트

N = int(input().rstrip())
for _ in range(N):
    command = input().rstrip().split()
    if command[0] == '1':
        stack.push(int(command[1]))
    elif command[0] == '2':
        result.append(str(stack.pop()))
    elif command[0] == '3':
        result.append(str(stack.size()))
    elif command[0] == '4':
        result.append('1' if stack.is_empty() else '0')
    elif command[0] == '5':
        result.append(str(stack.top()))

sys.stdout.write('\n'.join(result))