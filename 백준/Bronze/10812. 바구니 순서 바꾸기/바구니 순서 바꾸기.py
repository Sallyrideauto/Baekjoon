def rotate(baskets, begin, end, mid):
    left = baskets[:begin-1]
    right = baskets[end:]
    target = baskets[begin-1:end]
    target = target[mid-begin:] + target[:mid-begin]
    return left + target + right

def print_baskets(baskets):
    print(" ".join(map(str, baskets)))

n, m = map(int, input().split())
baskets = list(range(1, n+1))
for _ in range(m):
    i, j, k = map(int, input().split())
    baskets = rotate(baskets, i, j, k)
print_baskets(baskets)
