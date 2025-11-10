S, K, H = map(int, input().split())

school_score = []
school_score.append(S)
school_score.append(K)
school_score.append(H)

minimum = min(school_score)

participation_rate = S + K + H

if participation_rate >= 100:
    print("OK")
elif minimum == S:
    print("Soongsil")
elif minimum == K:
    print("Korea")
elif minimum == H:
    print("Hanyang")