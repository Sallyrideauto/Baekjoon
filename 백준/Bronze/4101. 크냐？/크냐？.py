while True:
    A, B = map(int, input().split())
    if A > 0 and B > 0:
        if A > B:
            print("Yes")
        else:
            print("No")
    elif A == 0 and B == 0:
        break