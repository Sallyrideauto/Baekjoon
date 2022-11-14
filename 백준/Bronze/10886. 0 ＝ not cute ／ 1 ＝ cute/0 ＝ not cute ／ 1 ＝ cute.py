N = int(input())
cute = []
ncute = []

for i in range(N):
    i = int(input())
    if i == 1:
        cute.append(i)
    elif i == 0:
        ncute.append(i)

if len(cute) > len(ncute):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")