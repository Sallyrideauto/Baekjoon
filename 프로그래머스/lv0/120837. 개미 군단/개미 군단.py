def solution(hp):
    if hp == 0:
        return 0
    
    memo = [-1 for _ in range(hp+1)]
    
    def ant(hp):
        if hp == 0:
            return 0
        if memo[hp] != -1:
            return memo[hp]
        
        memo[hp] = float('inf')
        
        # 장군개미 5마리로 공격
        if hp >= 5:
            memo[hp] = min(memo[hp], ant(hp-5)+1)
        
        # 병정개미 3마리로 공격
        if hp >= 3:
            memo[hp] = min(memo[hp], ant(hp-3)+1)
        
        # 일개미 1마리로 공격
        memo[hp] = min(memo[hp], ant(hp-1)+1)
        
        return memo[hp]
    
    return ant(hp)