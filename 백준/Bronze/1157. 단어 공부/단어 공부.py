word = input().upper()  # 대소문자 구분 없이 처리하기 위해 모두 대문자로 바꿈
count = [0] * 26  # 알파벳 수(26개)만큼 리스트 초기화

for char in word:
    if char.isalpha():
        count[ord(char) - ord('A')] += 1

max_count = max(count)  # 가장 많이 사용된 알파벳의 개수
max_char = '?'  # 가장 많이 사용된 알파벳이 여러 개인 경우를 대비한 초기값

if count.count(max_count) == 1:  # 가장 많이 사용된 알파벳이 유일한 경우
    max_char = chr(count.index(max_count) + ord('A'))  # 해당 알파벳 출력
print(max_char)
