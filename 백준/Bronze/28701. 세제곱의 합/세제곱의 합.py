N = int(input())
sum_val = 0
sum_val_3 = 0

for i in range(1, N + 1):
    sum_val += i
    sum_val_3 += (i ** 3)

print(sum_val)
print(sum_val ** 2)
print(sum_val_3)