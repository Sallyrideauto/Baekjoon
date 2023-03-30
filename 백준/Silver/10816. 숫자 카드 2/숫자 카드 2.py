"""
다음은 상근이가 가지고 있는 숫자 카드를 딕셔너리로 만든 뒤, 
입력된 M개의 수가 딕셔너리에 있는지 확인하여 개수를 출력하는 파이썬 프로그램입니다.
"""

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card_dict = {}
for card in cards:
    if card not in card_dict:
        card_dict[card] = 1
    else:
        card_dict[card] += 1

for num in nums:
    if num in card_dict:
        print(card_dict[num], end=' ')
    else:
        print(0, end=' ')
