# 좋은 단어의 개수를 세는 함수
def count_good_words(n, words):
    good_word_count = 0
    
    for word in words:
        stack = []
        
        for char in word:
            if stack and stack[-1] == char:
                # 스택이 비어 있지 않고, 스택의 맨 위와 현재 문자가 같으면
                stack.pop()
            else:
                stack.append(char)    # 그렇지 않으면 현재 문자를 스택에 추가
                
        if not stack:
            # 스택이 비어 있으면 모든 문자가 짝을 구성한 것
            good_word_count += 1
            
    return good_word_count

n = int(input())
words = [input().strip() for _ in range(n)]

print(count_good_words(n, words))