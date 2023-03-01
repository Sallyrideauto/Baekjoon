n, m = map(int, input().split())

preferences = []
for i in range(n):
    subject, fruit, color = input().split()
    preferences.append((subject, fruit, color))

for i in range(m):
    query = input().split()
    subject, fruit, color = query[0], query[1], query[2]
    count = 0
    for j in range(n):
        if (subject == '-' or subject == preferences[j][0]) and \
           (fruit == '-' or fruit == preferences[j][1]) and \
           (color == '-' or color == preferences[j][2]):
            count += 1
    print(count)
