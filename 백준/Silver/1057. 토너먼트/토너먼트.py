def tournament(N, kim, lim):
    round_num = 0
    while kim != lim:
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2
        round_num += 1
    return round_num
    
N, kim, lim = map(int, input().split())

print(tournament(N, kim, lim))