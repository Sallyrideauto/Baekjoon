n = int(input())  # 전체 사람의 수

people = []  # 각 사람의 정보를 저장할 리스트

# 입력을 받아 각 사람의 정보를 리스트에 추가
for i in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

rank = []  # 각 사람의 덩치 등수를 저장할 리스트

# 모든 사람에 대해 덩치 등수를 계산
for i in range(n):
    count = 1  # 자신보다 큰 덩치의 사람 수를 저장할 변수
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    rank.append(str(count))

print(' '.join(rank))  # 덩치 등수 출력
