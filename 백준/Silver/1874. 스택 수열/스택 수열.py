n = int(input())
stack = []
result = []
count = 1

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))

"""
여기서 발생 가능한 문제는 입력값이 매우 큰 경우 스택에 넣고 뽑는 과정에서 시간 초과가 발생할 수 있다는 것입니다. 
이를 해결하기 위해서는 스택에 들어있는 마지막 숫자와 비교해야 하는 data가 매우 큰 경우 시간이 오래 걸리기 때문에 다음과 같이 수정할 수 있습니다.

1. 입력값을 모두 리스트에 저장합니다.
2. 현재 스택에 들어있는 수와 다음에 push할 수를 비교합니다.
3. 다음에 push할 수보다 현재 스택에 들어있는 수가 작으면 스택에서 pop합니다.
4. 다음에 push할 수까지 스택에 push합니다.
5. 스택이 비었을 때, 입력값 리스트에서 data를 제거합니다.

이렇게 하면 스택에 넣고 뽑는 과정이 줄어들기 때문에 시간 복잡도가 줄어들어 시간 초과를 예방할 수 있습니다.
"""