# 테스트 케이스의 수 입력
t = int(input())

# 테스트 케이스만큼 반복
for i in range(t):
    # 괄호 문자열 입력
    ps = input()
    stack = []
    is_vps = True
    
    # 괄호 문자열 순회
    for p in ps:
        # 여는 괄호면 스택에 추가
        if p == '(':
            stack.append(p)
        # 닫는 괄호면 스택에서 제거
        elif p == ')':
            # 스택이 비어있으면 VPS가 아님
            if not stack:
                is_vps = False
                break
            # 짝이 맞지 않으면 VPS가 아님
            if stack[-1] == '(':
                stack.pop()
            else:
                is_vps = False
                break
    
    # 스택에 여는 괄호가 남아있으면 VPS가 아님
    if stack:
        is_vps = False
        
    # 결과 출력
    if is_vps:
        print('YES')
    else:
        print('NO')
