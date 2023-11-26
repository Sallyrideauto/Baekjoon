import sys

s = sys.stdin.readline().rstrip().split('-')
s_arr = []

for i in range(len(s)):
    initial = list(s[i])
    s_arr.append(initial[0])

for elem in s_arr:
    print(elem, end = '')