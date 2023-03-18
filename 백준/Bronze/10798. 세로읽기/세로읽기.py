words = []
for i in range(5):
    word = input()
    words.append(word)

max_len = max(len(word) for word in words)

result = ""
for j in range(max_len):
    for i in range(5):
        if j < len(words[i]):
            result += words[i][j]

print(result)
