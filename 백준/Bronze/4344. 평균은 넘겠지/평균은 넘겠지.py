# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for i in range(T):
    # 학생 수와 점수를 입력받습니다.
    scores = list(map(int, input().split()))
    # 학생 수와 점수를 분리합니다.
    N = scores[0]
    scores = scores[1:]
    # 평균을 구합니다.
    avg = sum(scores) / N
    # 평균을 넘는 학생들의 비율을 구합니다.
    count = sum([1 for score in scores if score > avg])
    ratio = count / N * 100
    # 결과를 출력합니다.
    print("{:.3f}%".format(ratio))