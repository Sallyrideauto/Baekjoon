def main():
    n, l = map(int, input().split())
    for i in range(l, 101):
        if (2 * n + i - i * i) % (2 * i) == 0:
            start = (2 * n + i - i * i) // (2 * i)
            if start < 0:
                continue
            for j in range(i):
                print(start + j, end=' ')
            return
    print(-1)

if __name__ == '__main__':
    main()