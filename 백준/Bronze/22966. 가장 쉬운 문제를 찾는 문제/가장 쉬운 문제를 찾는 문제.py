N = int(input())
test = []

for i in range(N):
    title, lev = map(str, input().split())
    lev = int(lev)
    test.append([title, lev])

test.sort(key = lambda x : x[1])

print(test[0][0])