def replace_lowercase(A, B):
    for b in B:
        A = A.replace(b, b.lower())
    return A

# 입력 받기
A = input()
B = input().split()

# 결과 출력
C = replace_lowercase(A, B)
print(C)