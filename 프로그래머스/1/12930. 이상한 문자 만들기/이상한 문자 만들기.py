def solution(s):
    # 단어별로 처리
    def convert_word(word):
        result = ''
        for i, char in enumerate(word):
            if i % 2 == 0:  # 짝수번째 문자
                result += char.upper()
            else:   # 홀수번째 문자
                result += char.lower()
        return result
    
    # 공백을 기준으로 문자열 분리 후, 각 단어별로 convert_word 함수를 적용
    return ' '.join(convert_word(word) for word in s.split(' '))