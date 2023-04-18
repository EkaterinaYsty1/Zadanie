print("Введите числа через пробел")
a = [int(x) for x in input().split()]
b = len(a)
for i in range(1, b):
    for j in range(b - 1, i - 1, -1):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
print(*a)