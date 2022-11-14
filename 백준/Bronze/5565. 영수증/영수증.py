total = int(input())
contents = []

for i in range(9):
    i = int(input())
    contents.append(i)

print(total - sum(contents))