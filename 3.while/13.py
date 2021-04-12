try:
    number = int(input("введите число : "))
    print("Введенное число", number)
except ValueError:
    print("Проебразование не удалось")
print("Завершение программы")