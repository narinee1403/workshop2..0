i = p = 0
x = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
while i < 11:
    print("   [" + str(x[i]) + "]   ")
    while p in range(12):
        print(str(x[i]) + " * " + str(y[p]) + " = " + str(x[i] * y[p]))
        p = p + 1
    print("-------------")
    p = 0
    i = i + 1


# for
i = p = 0
x = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in range(11):
    print("   [" + str(x[i]) + "]   ")
    for p in range(12):
        print(str(x[i]) + " * " + str(y[p]) + " = " + str(x[i] * y[p]))
        p = p + 1
    print("-------------")
    p = 0
    i = i + 1
