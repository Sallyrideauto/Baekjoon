# 주어진 단어에서 CAMBRIDGE에 포함된 알파벳을 모두 제거

word = input()  # 입력받은 단어

camb = 'CAMBRIDGE'  # 검열할 알파벳

for c in word:  # 단어의 각 알파벳에 대해
    if c not in camb:  # 만약 CAMBRIDGE에 포함되지 않는 알파벳이면
        print(c, end='')  # 출력

# 위 코드를 실행하면 입력받은 단어에서 CAMBRIDGE에 포함된 알파벳을 모두 제거한 결과가 출력됩니다.