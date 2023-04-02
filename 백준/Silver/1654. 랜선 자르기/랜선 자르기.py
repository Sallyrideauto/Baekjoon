k, n = map(int, input().split())
lan_cables = []
for _ in range(k):
    lan_cables.append(int(input()))

start, end = 1, max(lan_cables)

while start <= end:
    mid = (start + end) // 2
    cnt = sum([x // mid for x in lan_cables])
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)

"""
이진 탐색을 활용하여 주어진 k개의 랜선을 잘라서 n개의 같은 길이의 랜선을 만들어낼 수 있는 최대 길이를 구하는 문제입니다.

우선 입력받은 k개의 랜선 길이를 리스트에 저장하고, 이진 탐색을 위해 start와 end를 초기화합니다. 
이진 탐색의 기준이 되는 mid값은 start와 end의 중간값입니다.

mid를 기준으로 k개의 랜선을 잘라서 만들어낼 수 있는 랜선의 개수(cnt)를 구합니다. 
여기서는 각 랜선의 길이를 mid로 나눈 몫을 더한 값이 cnt가 됩니다.

cnt가 n보다 크거나 같으면, 랜선을 더 길게 잘라도 n개를 만들어낼 수 있으므로 start를 mid+1로 변경해줍니다. 
반대로 cnt가 n보다 작으면, 랜선을 더 짧게 잘라야 n개를 만들어낼 수 있으므로 end를 mid-1로 변경해줍니다.

이 과정을 반복하다가 start > end가 되면 최대 길이는 end가 됩니다. 
이유는 start가 end를 넘어서면 mid값이 start를 지나 end보다 더 큰 값을 갖게 되기 때문입니다.

마지막으로 구해진 최대 길이를 출력해줍니다.
"""