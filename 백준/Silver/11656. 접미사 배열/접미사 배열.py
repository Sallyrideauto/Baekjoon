s = input().strip()    # 입력받은 문자열을 공백 제거 후 저장
suffixes = []    # 접미사 저장을 위한 리스트

# 모든 접미사 생성 및 저장
for i in range(len(s)):
    suffixes.append(s[i:])
    
# 접미사 리스트 사전 순 정렬
suffixes.sort()

# 정렬된 접미사 출력
for suffix in suffixes:
    print(suffix)