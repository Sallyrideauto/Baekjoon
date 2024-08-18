import string

caesar_code = string.ascii_uppercase[3:] + string.ascii_uppercase[:3]
origin_s = string.ascii_uppercase

word = input()
word_trans = word.maketrans(caesar_code, origin_s)

print(word.translate(word_trans))