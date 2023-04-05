word = input()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in word:
    if char in vowels:
        count += 1
print(count)

"""
입력으로 주어진 단어를 word 변수에 저장하고, 모음을 리스트 vowels에 저장합니다. 
그리고 모음의 개수를 저장할 count 변수를 0으로 초기화합니다. 
이후 for 반복문을 사용하여 word에 있는 모든 문자들을 차례대로 탐색하면서, 모음인 경우 count를 1씩 증가시킵니다. 
마지막으로 count 값을 출력하여 모음의 개수를 출력합니다.
"""