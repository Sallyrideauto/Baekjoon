# 무한 루프를 실행하면서 계속 입력을 받음
while True:
    try:
        print(input())
    except EOFError:    # 입력의 끝을 나타냄
        break