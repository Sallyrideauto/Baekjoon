def solution(n, words):
    used_words = set() # 이미 사용된 단어 저장하는 set
    prev_word = words[0][0] # 첫 단어의 첫 글자로 시작
    
    for i, word in enumerate(words):
        if word in used_words or prev_word != word[0]: # 이미 사용한 단어거나, 첫 글자가 이전 단어와 다르면
            return [(i % n) + 1, (i // n) + 1] # 탈락자의 번호와 차례 반환
        
        used_words.add(word) # 사용한 단어 추가
        prev_word = word[-1] # 마지막 글자로 시작
    
    return [0, 0] # 탈락자가 없을 경우
