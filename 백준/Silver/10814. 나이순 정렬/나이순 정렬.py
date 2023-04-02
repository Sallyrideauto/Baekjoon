n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name)) # (나이, 가입 순서, 이름) 형태로 저장

members.sort() # 나이 기준으로 오름차순 정렬

for member in members:
    print(member[0], member[2]) # 나이와 이름 출력

"""
나이와 이름이 공백으로 구분되어 입력되기 때문에 split() 함수를 사용하여 나이와 이름을 나누어 리스트에 저장합니다. 
그리고 (나이, 가입 순서, 이름) 형태로 저장하는데, 가입 순서는 이후에 나이가 같을 경우 가입한 순서대로 정렬하기 위한 용도입니다.

그리고 sort() 함수를 사용하여 members 리스트를 나이를 기준으로 오름차순 정렬합니다. 
정렬할 때는 나이가 같을 경우 가입 순서가 우선적으로 고려됩니다.

마지막으로 for 문을 사용하여 정렬된 members 리스트를 순회하며 나이와 이름을 출력합니다. 
출력할 때는 member 튜플의 0번째 인덱스와 2번째 인덱스를 사용하여 나이와 이름을 출력합니다.
"""