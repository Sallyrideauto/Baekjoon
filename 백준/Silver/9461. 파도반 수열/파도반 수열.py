def find_pado_sequence(n):
    # 최대 길이 100까지의 수열을 저장할 리스트 초기화
    p = [0] * 101
    p[1], p[2], p[3] = 1, 1, 1
    for i in range(4, 101):
        p[i] = p[i - 2] + p[i - 3]
        
    return p[n]    # 결과 반환

# 테스트 케이스 입력 받기
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    results.append(find_pado_sequence(N))
    
# 결과 출력
for result in results:
    print(result)