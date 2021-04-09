year = int(input("Введите год : "))
if year < 0 or year > 30000:
    print("Неправильный год")
else :
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
        print("YES")
    else :
        print("NO")

