def dfs(start, cnt):
    if cnt == 6:
        print(' '.join(map(str, comb)))
        return
    for i in range(start, k):
        comb[cnt] = s[i]
        dfs(i+1, cnt+1)

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    k, s = lst[0], lst[1:]
    comb = [0] * 6
    dfs(0, 0)
    print()

    
"""
이 문제는 DFS를 활용하여 구할 수 있다. 
전체 집합에서 6개의 숫자를 선택해야 하므로, 
DFS 함수 내에서 선택한 개수(cnt)가 6이 되면 그때까지 선택한 숫자들을 출력하면 된다.

주의할 점은 숫자의 중복 선택을 피하기 위해, 
다음 선택할 수 있는 숫자의 범위를 현재 선택한 숫자보다 큰 범위로 설정해야 한다. 
이를 위해 DFS 함수 내에서 사용하는 start 매개변수를 설정하면 된다.

또한, 테스트 케이스 사이에 빈 줄을 출력해야 하므로, 
각각의 테스트 케이스마다 출력을 마치면 print()를 통해 빈 줄을 출력한다.
"""