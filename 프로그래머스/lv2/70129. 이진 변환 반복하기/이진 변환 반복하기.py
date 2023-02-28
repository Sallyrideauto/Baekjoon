def solution(s):
    count = 0  # 이진 변환의 횟수를 담을 변수
    remove_count = 0  # 변환 과정에서 제거된 0의 개수를 담을 변수
    
    # s가 "1"이 될 때까지 반복
    while s != "1":
        count += 1  # 이진 변환의 횟수 증가
        # 0 제거 및 1의 개수 세기
        remove_count += s.count("0")  
        s = s.replace("0", "")
        if s != "":
            s = bin(len(s))[2:]  # 이진 변환
    
    return [count, remove_count]
