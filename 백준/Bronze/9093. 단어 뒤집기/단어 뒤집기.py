def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

T = int(input())

for _ in range(T):
    sentence = input().strip()
    print(reverse_words(sentence))

"""
이 프로그램은 먼저 테스트 케이스의 개수 T를 입력 받습니다. 
그런 다음 각 테스트 케이스에 대해 문장을 입력 받고, 
reverse_words 함수를 호출하여 각 단어를 뒤집은 결과를 출력합니다.
"""