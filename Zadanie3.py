a = input("Введите строку ")
b = ""
с = False
for i in range(len(a)):
    if a[i] == "(":
        с = True
    elif a[i] == ")":
        с = False
    else:
        if not с:
           b += a[i]
print(b)