notes = list(map(int, input().split()))

if notes == sorted(notes):
    print("ascending")
elif notes == sorted(notes, reverse=True):
    print("descending")
else:
    print("mixed")

    
"""
위 코드는 입력받은 8개의 숫자를 리스트로 변환한 뒤, 
이 리스트가 오름차순으로 정렬되어 있는지, 내림차순으로 정렬되어 있는지, 
그 외의 경우 (혼합) 중 어느 것인지 판별하여 출력하는 프로그램입니다.
"""