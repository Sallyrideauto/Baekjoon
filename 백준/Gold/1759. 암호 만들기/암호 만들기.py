from itertools import combinations

def valid_password(password):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in password:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
            
    return vowel_count >= 1 and consonant_count >= 2

def generate_passwords(L, C, characters):
    passwords = []
    for comb in combinations(characters, L):
        password = ''.join(sorted(comb))
        if valid_password(password):
            passwords.append(password)
    return passwords

def main():
    L, C = map(int, input().split())
    characters = sorted(input().split())
    passwords = generate_passwords(L, C, characters)
    
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()

"""
이 프로그램은 가능한 암호를 생성하는 generate_passwords 함수를 사용합니다. 
이 함수는 주어진 문자들로부터 길이 L의 조합을 구한 다음, 그 조합이 유효한 암호인지 검사합니다. 
유효한 암호는 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있는 암호입니다. 
프로그램은 가능한 모든 암호를 출력합니다.
"""