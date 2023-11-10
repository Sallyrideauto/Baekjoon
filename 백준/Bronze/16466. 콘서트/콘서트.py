N = int(input())
sold_ticket = set(map(int, input().split()))

i = 1
while i in sold_ticket:
    i += 1

print(i)