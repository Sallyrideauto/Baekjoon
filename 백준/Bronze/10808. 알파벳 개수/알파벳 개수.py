# https://my-coding-notes.tistory.com/177
# 문자열 유니코드에 대한 학습 필요

s = list(input())
r = [0 for i in range(26)]

for i in s:
    r[ord(i) - 97] += 1

print(*r)