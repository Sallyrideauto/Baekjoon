# https://blog.naver.com/nkj2001/222698193629
# https://songsw.tistory.com/30
# 출력 형식에 대한 학습 필ㅑ

N = int(input())

for i in range(1, N + 1):
    print("*" * i + " " * (N * 2 - i * 2) + "*" * i)

for i in range(N - 1, 0, -1):
    print("*" * i + " " * (N * 2 - i * 2) + "*" * i)