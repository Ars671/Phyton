y = int(input("Введите количество операций: "))
first = int(input("Введите первое число: "))
i = 0
while i < y:
   e = input("Введите операцию: ")
   if e =="+":
    second = int(input("Введите число: "))
    first = first + second
    print(f"Результат {first}")
   elif e=="-":
    second = int(input("Введите число: "))
    first = first - second
    print(f"Результат {first}")
   elif e=="*":
    second = int(input("Введите число: "))
    first = first * second
    print(f"Результат {first}")
   elif e=="/":
    second = int(input("Введите число: "))
    if second == 0 :
        print("Ошибка")
    else:
        first = first / second
        print(f"Результат {first}")
   i+=1

