def main():
    D, N = map(int, input().split())
    oven = list(map(int, input().split()))
    pizzas = list(map(int, input().split()))

    # 오븐 지름을 오븐의 위에서부터 그보다 큰 값들을 제거
    for i in range(1, D):
        oven[i] = min(oven[i], oven[i-1])

    position = D - 1
    for pizza in pizzas:
        # 피자가 들어갈 위치 찾기
        while position >= 0 and oven[position] < pizza:
            position -= 1

        if position < 0:
            print(0)
            return
        position -= 1

    print(position + 2)


if __name__ == "__main__":
    main()

"""
이 프로그램은 오븐의 지름을 최상단부터 아래로 확인하면서, 각 위치에서 오븐의 지름보다 큰 피자 반죽을 제거합니다. 
그런 다음 피자 반죽을 순서대로 오븐에 넣으면서 각 피자 반죽이 들어갈 수 있는 위치를 찾습니다. 
마지막으로 맨 위의 피자의 위치를 출력합니다. 
만약 피자가 모두 오븐에 들어가지 않는 경우, 0을 출력합니다.
"""