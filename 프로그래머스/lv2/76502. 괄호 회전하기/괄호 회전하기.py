def solution(s):
    def is_valid(s):
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            elif c in [")", "}", "]"]:
                if not stack:
                    return False
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    
    answer = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            answer += 1
    return answer