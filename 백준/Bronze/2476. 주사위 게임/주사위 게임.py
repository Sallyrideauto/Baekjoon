def prize(rolls):
    count = [0] * 7
    for roll in rolls:
        count[roll] += 1
    for i in range(1, 7):
        if count[i] == 3:
            return 10000 + i * 1000
        elif count[i] == 2:
            return 1000 + i * 100
    return max(rolls) * 100

def main():
    N = int(input())
    max_prize = 0
    for _ in range(N):
        rolls = list(map(int, input().split()))
        current_prize = prize(rolls)
        if current_prize > max_prize:
            max_prize = current_prize
    print(max_prize)

if __name__ == "__main__":
    main()

"""
이 프로그램은 입력된 참여자들의 주사위 눈을 바탕으로 상금을 계산한 후, 
가장 큰 상금을 찾아 출력합니다. 
주어진 주사위 눈에 따라 상금 계산 규칙을 적용하고 있습니다.
"""