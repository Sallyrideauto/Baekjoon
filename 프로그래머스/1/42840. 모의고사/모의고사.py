def solution(answers):
    # 각 수포자가 찍는 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자의 점수를 계산
    score1 = sum([1 for i, answer in enumerate(answers) if answer == pattern1[i % len(pattern1)]])
    score2 = sum([1 for i, answer in enumerate(answers) if answer == pattern2[i % len(pattern2)]])
    score3 = sum([1 for i, answer in enumerate(answers) if answer == pattern3[i % len(pattern3)]])
    
    # 가장 많이 맞힌 점수를 계산
    max_score = max(score1, score2, score3)
    
    # 가장 많이 맞힌 수포자를 결과 리스트에 추가
    result = []
    if score1 == max_score:
        result.append(1)
    if score2 == max_score:
        result.append(2)
    if score3 == max_score:
        result.append(3)
        
    return result