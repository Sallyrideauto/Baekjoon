# 윷놀이 함수
def yoot_game(yoots):
    # 배가 나온 횟수를 세는 변수
    num_back = yoots.count(0)
    # 등이 나온 횟수를 세는 변수
    num_front = yoots.count(1)
    
    # 결과에 따라 출력할 문자열을 저장하는 변수
    result = ''
    
    # 배와 등의 개수에 따라 결과 문자열을 결정
    if num_back == 1 and num_front == 3:
        result = 'A'
    elif num_back == 2 and num_front == 2:
        result = 'B'
    elif num_back == 3 and num_front == 1:
        result = 'C'
    elif num_back == 4:
        result = 'D'
    elif num_front == 4:
        result = 'E'
    
    return result

# 윷놀이 결과 출력
for i in range(3):
    yoots = list(map(int, input().split()))
    print(yoot_game(yoots))

"""
위 프로그램은 윷놀이 게임에서 주어진 윷짝 네 개를 입력받아 결과를 출력하는 프로그램입니다. 
입력받은 윷짝들의 배(0)와 등(1)의 개수를 세어 결과에 따라 문자열을 결정하고, 그 결과를 출력합니다. 
반복문을 이용하여 세 번의 입력과 결과 출력을 반복합니다.
"""