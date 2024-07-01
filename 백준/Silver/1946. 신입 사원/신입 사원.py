import sys
input = sys.stdin.read

def count_qualified_candidates():
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        applicants = []
        
        for _ in range(N):
            paper, interview = map(int, data[index:index+2])
            applicants.append((paper, interview))
            index += 2
        
        # 서류 순위로 정렬
        applicants.sort()
        
        max_interview_rank = float('inf')
        count = 0
        
        for paper, interview in applicants:
            if interview < max_interview_rank:
                max_interview_rank = interview
                count += 1
        
        results.append(count)
    
    for result in results:
        print(result)

# 함수 호출
count_qualified_candidates()
