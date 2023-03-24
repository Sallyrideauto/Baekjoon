def compress(x, y, n):
    global result
    check = image[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != image[i][j]:
                result += "("
                compress(x, y, n//2) # 왼쪽 위
                compress(x, y+n//2, n//2) # 오른쪽 위
                compress(x+n//2, y, n//2) # 왼쪽 아래
                compress(x+n//2, y+n//2, n//2) # 오른쪽 아래
                result += ")"
                return
    result += str(check)

n = int(input())
image = [input() for _ in range(n)]
result = ""
compress(0, 0, n)
print(result)
