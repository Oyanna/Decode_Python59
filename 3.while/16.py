try:
    number = int(input())
    print(number)
except ValueError as e:
    print("Сведения об исключении", e)