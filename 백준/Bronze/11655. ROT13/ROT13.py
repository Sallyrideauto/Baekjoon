def ROT13(s):
    result = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

S = input()
encrypted = ROT13(S)
print(encrypted)
