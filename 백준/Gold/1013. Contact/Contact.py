import re

def is_valid_contact(s):
    # 정규 표현식 패턴
    pattern = re.compile(r'(100+1+|01)+')
    
    # 전체 문자열이 패턴과 일치하는지 확인
    return pattern.fullmatch(s) is not None

n = int(input())
for _ in range(n):
    s = input().strip()
    if is_valid_contact(s):
        print("YES")
    else:
        print("NO")