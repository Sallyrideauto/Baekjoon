friends = []
while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    sum = (M + F)
    friends.append(sum)

for i in friends:
    print(i)