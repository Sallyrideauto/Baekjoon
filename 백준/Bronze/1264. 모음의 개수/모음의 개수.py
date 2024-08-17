while True:
    s = input()
    cnt = 0
    
    if s == '#':
        break
    
    for ch in s:
        if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            cnt += 1
            
    print(cnt)