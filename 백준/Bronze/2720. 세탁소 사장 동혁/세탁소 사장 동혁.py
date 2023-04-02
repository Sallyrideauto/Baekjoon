T = int(input())

for _ in range(T):
    C = int(input())
    quarters = C // 25
    C %= 25
    dimes = C // 10
    C %= 10
    nickels = C // 5
    C %= 5
    pennies = C
    print(quarters, dimes, nickels, pennies)

    
"""
센트 단위의 거스름돈을 받아서, 쿼터, 다임, 니켈, 페니의 개수를 구하는 문제입니다. 
거슬러 줄 수 있는 동전은 쿼터(25센트), 다임(10센트), 니켈(5센트), 페니(1센트)입니다.

위의 코드에서 quarters, dimes, nickels, pennies 변수는 각각 거슬러 줄 쿼터, 다임, 니켈, 페니의 개수입니다. 
C는 거슬러 줘야 할 거스름돈의 총 액수입니다. 
먼저 quarters 변수에 C를 25로 나눈 몫을 할당하고, C에서 25로 나눈 나머지를 다시 C에 할당합니다. 
이후, dimes, nickels, pennies 변수에 대해서도 위와 같은 방법으로 거슬러 줄 동전의 개수를 구합니다.

마지막으로, 각각의 거슬러 줄 동전의 개수를 출력합니다. 
출력할 때는 print() 함수를 사용하고, 출력할 변수들을 공백으로 구분하여 함수에 전달합니다.
"""