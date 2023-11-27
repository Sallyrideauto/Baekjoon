A, B, C, D = input().split()

AB_arr, CD_arr = [], []

AB_arr.append(A)
AB_arr.append(B)
CD_arr.append(C)
CD_arr.append(D)

AB, CD = ''.join(AB_arr), ''.join(CD_arr)
AB, CD = int(AB), int(CD)

print(AB + CD)