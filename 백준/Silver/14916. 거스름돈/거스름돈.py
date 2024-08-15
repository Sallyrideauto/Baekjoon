n = int(input())

# 예외 처리: 1, 3원은 거슬러 줄 수 없음
if n == 1 or n == 3:
    print(-1)
else:
    # 5원 동전 사용을 최대한 우선순위로 처리
    cnt = 0
    while n > 0:
        if n % 5 == 0:  # 5의 배수이면 5원 동전으로 거슬러 줄 수 있음
            cnt += n // 5
            break
        n -= 2  # 5의 배수가 아니면 2원 동전 사용
        cnt += 1
        
    print(cnt)