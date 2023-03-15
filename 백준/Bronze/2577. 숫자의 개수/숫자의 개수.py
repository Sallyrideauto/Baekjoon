a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

for i in range(10):
    count = result.count(str(i))
    print(count)
