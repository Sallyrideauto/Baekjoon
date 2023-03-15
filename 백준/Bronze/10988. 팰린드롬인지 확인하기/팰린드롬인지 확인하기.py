word = input()

# 단어의 길이를 저장합니다.
length = len(word)

# 단어의 절반까지만 반복합니다.
for i in range(length // 2):
    # 앞쪽 문자와 뒤쪽 문자를 비교합니다.
    if word[i] != word[length - i - 1]:
        print(0)
        break
else:
    print(1)
