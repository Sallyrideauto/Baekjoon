n = int(input())
count = n

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]: # 현재 문자와 다음 문자가 다르면
            if word[j] in word[j+1:]: # 현재 문자가 이후에 또 등장하면
                count -= 1 # 그룹 단어가 아니므로 count에서 제외
                break # 더 이상 확인할 필요 없으므로 반복문 탈출

print(count)
