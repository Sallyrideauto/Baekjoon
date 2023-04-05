"""
아래는 입력값을 받고, 
검색 결과에서 첫 번째 파일 이름을 기준으로 각 문자열의 길이와 비교하여, 
문자열이 일치하면 그 문자를 그대로, 
일치하지 않으면 ?를 출력하는 코드입니다.
"""

n = int(input()) # 파일 이름의 개수
file_names = []
for _ in range(n):
    file_names.append(input()) # 파일 이름 리스트에 추가

pattern = ""
for i in range(len(file_names[0])):
    match = True # 모든 파일 이름이 해당 위치의 문자열이 일치하는지 확인하는 변수
    for j in range(1, n): # 첫 번째 파일 이름을 제외한 나머지 파일 이름 비교
        if file_names[0][i] != file_names[j][i]:
            match = False
            break
    if match:
        pattern += file_names[0][i]
    else:
        pattern += "?"
        
print(pattern)
