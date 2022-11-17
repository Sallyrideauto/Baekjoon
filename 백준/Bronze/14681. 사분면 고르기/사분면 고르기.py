# x, y = map(int, input().split()) // 런타임 에러 발생
# 두 개의 수를 한 번에 하나씩 입력받아야 함

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")