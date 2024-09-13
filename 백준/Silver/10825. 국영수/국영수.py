# 학생 수 입력
n = int(input())

# 학생 정보 입력 (이름, 국어, 영어, 수학)
students = []
for _ in range(n):
    name, korean, english, math = input().split()
    students.append((name, int(korean), int(english), int(math)))

# 정렬 기준에 따라 정렬
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 정렬된 학생들의 이름 출력
for student in students:
    print(student[0])
