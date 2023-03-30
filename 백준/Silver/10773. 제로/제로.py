stack = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))

"""
우선 스택을 이용하여 문제를 해결합니다. 
주어진 정수가 0일 경우에는 스택에서 가장 최근에 쓴 수를 지워야 합니다. 
따라서 pop() 함수를 사용하여 스택에서 가장 최근에 쓴 수를 지우고, 
아닐 경우에는 해당 수를 스택에 추가합니다. 
마지막으로 스택에 남아 있는 수들의 합을 출력하면 됩니다.
"""