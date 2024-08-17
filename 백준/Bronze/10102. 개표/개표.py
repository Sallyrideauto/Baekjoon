V = int(input())
candidates = input()
candidates_arr = list(candidates)

A_cnt = 0
B_cnt = 0

for i in range(len(candidates_arr)):
    if candidates_arr[i] == 'A':
        A_cnt += 1
    elif candidates_arr[i] == 'B':
        B_cnt += 1

if A_cnt > B_cnt:
    print('A')
elif B_cnt > A_cnt:
    print('B')
else:
    print('Tie')