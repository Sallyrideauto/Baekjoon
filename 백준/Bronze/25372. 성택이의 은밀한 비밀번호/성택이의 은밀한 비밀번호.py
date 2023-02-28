import re

N = int(input())

for i in range(N):
    password = input().strip()
    if 6 <= len(password) <= 9 and bool(re.match('^[a-zA-Z0-9]+$', password)):
        print("yes")
    else:
        print("no")
