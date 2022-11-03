pieces = [1, 1, 2, 2, 2, 8]
having = list(map(int, input().split()))

for i in range(len(pieces)):
    print(pieces[i] - having[i])