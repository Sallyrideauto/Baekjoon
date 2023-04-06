"""
입력에서 주어지는 문자열 중에서 괄호가 균형을 이루지 않는 경우 "no"를 출력하면 됩니다. 
이를 판단하기 위해서는 스택 자료구조를 활용하면 됩니다.
"""

while True:
    s = input()
    if s == ".":
        break
    stack = []
    is_balanced = True
    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if not stack or stack[-1] != "(":
                is_balanced = False
                break
            stack.pop()
        elif c == "]":
            if not stack or stack[-1] != "[":
                is_balanced = False
                break
            stack.pop()
    if is_balanced and not stack:
        print("yes")
    else:
        print("no")

"""
이 코드는 문자열의 각 문자를 순서대로 탐색하면서 스택에 왼쪽 괄호를 저장하다가 오른쪽 괄호를 만나면 스택에서 짝이 맞는 왼쪽 괄호를 제거합니다.
문자열 전체를 탐색한 후에 스택이 비어있으면 균형잡힌 문자열이고, 그렇지 않으면 균형잡히지 않은 문자열입니다.
"""