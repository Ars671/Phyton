i = 1
num = 0
ret=0
r = 0
while (r < 31):
    r = r + 1
    sum = 0
    num = num + r
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    ret = ret + sum * 7
t = 0
while (t < 30):
    t = t + 1
    sum = 0
    num = num + t
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    ret = ret + sum * 4
y = 0
while (y < 28):
    y = y + 1
    sum = 0
    num = num + y
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    ret = ret + sum
print("Сумма цифр числа равна: ", ret)
       