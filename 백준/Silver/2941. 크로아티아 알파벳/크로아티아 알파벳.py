word = input()
croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in croatian_alphabet:
    word = word.replace(alpha, '*')

print(len(word))