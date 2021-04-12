try:
    num1 = int(input())
    num2 = int(input())
    print("Результат деления : ", num1/num2)
except ValueError:
    print("Неверный тип")
except ZeroDivisionError:
    print("Попытка деления на ноль")
except Exception:
    print("Какое-то общее исключение")
print("КОНЕЦ")