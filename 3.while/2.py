a=int(input("Введи 1 число\n"))
b=int(input("Введи 2 число\n"))
c=int(input("Введи 3 число\n"))
if a>=b and a>=c:
    print("Максимум равен ",a)
elif b>=a and b>=c:
    print("Максимум равен ",b)
else :
    print("Максимум равен ",c)