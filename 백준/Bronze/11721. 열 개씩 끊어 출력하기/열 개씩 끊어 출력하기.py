word = input()

for i in range(0, len(word), 10):
    print(word[i:i+10])

"""
우선 입력으로 주어진 단어를 input() 함수를 이용하여 입력 받습니다. 
그 다음, range() 함수를 이용하여 단어를 10글자씩 끊어서 반복문을 실행합니다. 
반복문에서는 print() 함수를 이용하여 10글자씩 출력합니다. 
단어의 길이가 10의 배수가 아닌 경우에도 마지막 줄에는 10개 미만의 글자만 출력됩니다.
"""