N = int(input())

if N % 4 == 0:
    longcal = "long " * (N // 4)
    result_rstrip = longcal.rstrip()
    print(f"{result_rstrip}", "int")