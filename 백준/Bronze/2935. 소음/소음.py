A = int(input())
calc_sign = input()
B = int(input())

if calc_sign == '+':
    print(A + B)
elif calc_sign == '*':
    print(A * B)
else:
    print("덧셈과 곱셈 기호만 입력 가능합니다.")