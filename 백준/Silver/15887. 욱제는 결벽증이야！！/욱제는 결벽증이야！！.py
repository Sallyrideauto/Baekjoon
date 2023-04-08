"""
이 문제는 그리디 알고리즘을 사용하여 해결할 수 있습니다. 
주어진 조건에 따라 카드 배열을 최적의 상태로 만드는 연산을 수행하는 프로그램을 작성해 보겠습니다.
"""

def card_arrangement(N, cards):
    operations = []

    for i in range(1, N + 1):
        if cards[i - 1] != i:
            for j in range(i, N):
                if cards[j] == i:
                    cards[i - 1:j + 1] = reversed(cards[i - 1:j + 1])
                    operations.append((i, j + 1))
                    break

    return operations

def main():
    N = int(input())
    cards = list(map(int, input().split()))
    operations = card_arrangement(N, cards)
    
    print(len(operations))
    for op in operations:
        print(op[0], op[1])

if __name__ == "__main__":
    main()

"""
이 프로그램은 주어진 입력에 따라 N과 카드 배열을 입력 받고, 
card_arrangement 함수를 사용하여 카드를 최적의 상태로 만들기 위해 필요한 연산의 횟수와 연산에 필요한 [L, R] 쌍을 출력합니다. 
연산의 횟수가 0이라면 아무것도 출력하지 않습니다.
"""