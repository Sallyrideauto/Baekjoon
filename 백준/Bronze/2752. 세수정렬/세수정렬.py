nums = []
a, b, c = map(int, input().split())
nums.append(a)
nums.append(b)
nums.append(c)

nums.sort()
print("{} {} {}".format(*nums))