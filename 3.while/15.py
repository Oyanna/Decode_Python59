try :
    number = int(input())
    print("Введенное число ", number)
except ValueError:
    print("Не удалось преобразовать")
finally:
    print("Блок try1 завершил выполнение")

print("КОНЕЦ")