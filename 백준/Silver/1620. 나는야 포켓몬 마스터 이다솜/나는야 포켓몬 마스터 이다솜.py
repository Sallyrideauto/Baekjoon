def solve():
    import sys
    input = sys.stdin.read
    
    # 데이터를 직접 입력받는 부분을 추가합니다.
    data = input().split()
    if not data:
        # 입력된 데이터가 없는 경우는 입력을 받도록 합니다.
        n, m = map(int, input().split())
        name_to_number = {}
        number_to_name = []
        
        for i in range(1, n + 1):
            name = input().strip()
            name_to_number[name] = i
            number_to_name.append(name)
        
        results = []
        for _ in range(m):
            query = input().strip()
            if query.isdigit():
                results.append(number_to_name[int(query) - 1])
            else:
                results.append(str(name_to_number[query]))
        
        for result in results:
            print(result)

    else:
        # 입력이 주어졌다면, 기존 코드를 실행합니다.
        N = int(data[0])
        M = int(data[1])
        
        name_to_number = {}
        number_to_name = []
        
        index = 2
        for i in range(1, N + 1):
            name = data[index]
            index += 1
            name_to_number[name] = i
            number_to_name.append(name)
        
        results = []
        for _ in range(M):
            query = data[index]
            index += 1
            if query.isdigit():
                results.append(number_to_name[int(query) - 1])
            else:
                results.append(str(name_to_number[query]))
        
        for result in results:
            print(result)

if __name__ == "__main__":
    solve()
