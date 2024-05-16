def calculate_blocks(n):
    return 2 ** n

n = int(input().strip())

blocks = calculate_blocks(n)
print(blocks)