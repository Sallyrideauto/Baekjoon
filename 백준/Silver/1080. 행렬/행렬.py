def flip(matrix, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = 1 - matrix[i][j]
            
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    A = [list(map(int, list(data[i + 2]))) for i in range(N)]
    B = [list(map(int, list(data[N + i + 2]))) for i in range(N)]
    
    def solve(A, B, N, M):
        cnt = 0
        for i in range(N - 2):
            for j in range(M - 2):
                if A[i][j] != B[i][j]:
                    flip(A, i, j)
                    cnt += 1
                    
        if A == B:
            return cnt
        else:
            return -1
        
    print(solve(A, B, N, M))
    
if __name__ == "__main__":
    main()