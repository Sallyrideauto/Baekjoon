def main():
    import sys
    input = sys.stdin.readline

    # 사람의 수 입력받기
    n = int(input().strip())
    
    # 친구 관계 정보 읽기 (문자열 리스트)
    friends = [input().strip() for _ in range(n)]
    
    max_count = 0  # 최대 2-친구 수를 저장할 변수
    
    # 각 사람 i에 대해 2-친구 집합을 구한다.
    for i in range(n):
        two_friends = set()
        
        # 직접 친구를 확인
        for j in range(n):
            if friends[i][j] == 'Y':
                two_friends.add(j)  # 직접 친구 추가
                
                # 친구의 친구를 확인
                for k in range(n):
                    if friends[j][k] == 'Y':
                        two_friends.add(k)
                        
        # 자기 자신은 제외
        if i in two_friends:
            two_friends.remove(i)
        
        # 현재 사람의 2-친구 수와 최댓값 비교
        max_count = max(max_count, len(two_friends))
    
    # 최종 결과 출력
    print(max_count)

if __name__ == '__main__':
    main()
