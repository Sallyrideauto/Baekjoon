import re

def solution(s):
    return re.sub(r'\b\w', lambda x: x.group().upper(), s.lower())