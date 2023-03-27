"""
sorted()는 리스트를 정렬하는 함수이며, 이를 이용해 첫 번째 조건인 "길이가 짧은 것부터"를 만족시킬 수 있습니다.
또한, sorted() 함수는 기본적으로 오름차순으로 정렬되기 때문에 "길이가 같으면 사전 순으로"를 만족시키기 위해서는 따로 설정할 필요가 없습니다.

중복된 단어는 하나만 남겨야 하기 때문에 set()을 이용해 중복을 제거할 수 있습니다.
"""

n = int(input())
words = [input().strip() for _ in range(n)]

# 중복 제거 후 길이 순으로 정렬
words = sorted(set(words), key=lambda x: (len(x), x))

# 결과 출력
for word in words:
    print(word)

"""
먼저 입력으로 받은 문자열들을 리스트 words에 저장합니다. 
중복을 제거하기 위해 set() 함수를 이용해 중복을 제거하고, 
이후 sorted() 함수를 이용해 "길이가 짧은 것부터"를 만족시키면서 
"길이가 같으면 사전 순으로"를 만족시키도록 정렬합니다.
마지막으로, 정렬된 결과를 출력합니다.
"""