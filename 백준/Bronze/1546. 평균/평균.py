N = input() # 과목의 수
mylist = list(map(int, input().split())) # 점수 정보가 담긴 리스트
mymax = max(mylist) # mylist의 최대값
sum = sum(mylist) # mylist의 모든 데이터값 더하기

# 총합*100/최고점수/과목수 계산 결과 출력
# 한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환해 로직을 간단하게 할 수 있음
print(sum * 100 / mymax / int(N))