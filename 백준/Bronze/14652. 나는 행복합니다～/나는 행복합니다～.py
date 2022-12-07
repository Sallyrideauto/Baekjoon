# https://somjang.tistory.com/entry/BaekJoon-14652%EB%B2%88-%EB%82%98%EB%8A%94-%ED%96%89%EB%B3%B5%ED%95%A9%EB%8B%88%EB%8B%A4-Python

def i_am_happy(N, M, K):
    # i + j * M = K
    i = K // M
    j = K % M

    return f"{i} {j}"


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    print(i_am_happy(N, M, K))