def solution(num):
    cnt = 0
    if num == 0:
        return 0
    else:
        while True:
            if num == 1:
                return cnt
            elif cnt >= 500:
                return -1
            if num % 2 == 0:
                num //= 2
                cnt += 1
            else:
                num = (num * 3) + 1
                cnt += 1