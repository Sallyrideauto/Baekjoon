minguk = list(map(int, input().split()))
mansei = list(map(int, input().split()))
S = sum(minguk)
T = sum(mansei)

if S > T:
    print(S)
elif S < T:
    print(T)
elif S == T:
    print(S)