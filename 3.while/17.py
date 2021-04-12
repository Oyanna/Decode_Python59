n = input("Введите число: ")

while type(n) != int:
    try :
        n = int(n)
    except ValueError:
        print("Вы ввели неверное число")
        n = input("Введите целое число: ")

if n % 2 == 0:
    print("ЧЕТНОЕ")
else :
    print("НЕЧЕТНОЕ")