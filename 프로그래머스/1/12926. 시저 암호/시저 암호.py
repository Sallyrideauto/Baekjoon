def solution(s, n):
    result = ''
    for char in s:
        # 소문자인 경우
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        # 대문자인 경우
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        # 공백인 경우
        else:
            result += char
    return result
        