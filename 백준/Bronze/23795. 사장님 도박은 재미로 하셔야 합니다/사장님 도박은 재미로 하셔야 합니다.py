gamble = []
while True:
    N = int(input())
    if N == -1:
        break
    gamble.append(N)

print(sum(gamble))