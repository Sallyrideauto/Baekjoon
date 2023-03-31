# 다음은 주어진 문자열에서 각 테스트 케이스마다 점수를 구하는 파이썬 코드이다.

n = int(input())

for i in range(n):
    quiz = input()
    score = 0
    combo = 0  # 연속된 O의 개수를 저장할 변수
    for ans in quiz:
        if ans == "O":
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)

"""
먼저 테스트 케이스의 개수를 입력받고, for 루프를 이용하여 각 테스트 케이스마다 점수를 계산한다. 
문자열을 입력받은 후, score 변수와 combo 변수를 초기화한다. 
combo 변수는 연속된 O의 개수를 저장할 변수이다. 문자열을 하나씩 읽어가며, 
만약 문자가 "O"이면 combo 변수를 1 증가시키고, score 변수에 combo 변수를 더한다. 
만약 문자가 "X"이면 combo 변수를 0으로 초기화한다. 마지막으로 score 변수를 출력한다.
"""