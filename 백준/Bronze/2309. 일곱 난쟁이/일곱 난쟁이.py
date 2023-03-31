dwarfs = []

# 아홉 난쟁이의 키를 입력 받음
for i in range(9):
    dwarfs.append(int(input()))

# 아홉 난쟁이 중 일곱 난쟁이의 키의 합이 100이 되는 경우를 찾음
for i in range(9):
    for j in range(i+1, 9):
        # 일곱 난쟁이의 키를 찾음
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            # 일곱 난쟁이의 키를 오름차순으로 정렬하여 출력
            ans = [x for k, x in enumerate(dwarfs) if k not in [i, j]]
            ans.sort()
            for a in ans:
                print(a)
            exit()

"""
프로그램은 먼저 아홉 난쟁이의 키를 입력 받습니다. 

그 다음, 아홉 난쟁이 중 일곱 난쟁이의 키의 합이 100이 되는 경우를 찾습니다. 
이를 위해 이중 for 루프를 사용하여 가능한 모든 두 명의 난쟁이를 선택합니다. 

그리고 이 중에서 일곱 난쟁이의 키를 찾습니다. 
이 때, 모든 아홉 난쟁이의 키의 합에서 두 명의 난쟁이의 키를 뺀 값이 100이 되면 일곱 난쟁이를 찾은 것입니다. 

마지막으로, 일곱 난쟁이의 키를 오름차순으로 정렬하여 출력합니다.
"""