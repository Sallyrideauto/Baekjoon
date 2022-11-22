JinhosMBTI = input()
N = int(input())
FriendsMBTI = [input() for _ in range(N)]
sameMBTI = []

for i in range(len(FriendsMBTI)):
    if JinhosMBTI == FriendsMBTI[i]:
        sameMBTI.append(FriendsMBTI[i])

print(len(sameMBTI))