class Person:
    def __init__(ab, name, age):
        ab.name = name
        ab.age = age

    def func1(ab):
        print("Привет, меня зовут " + ab.name)

p = Person("Ayana", 20)
p1 = Person("Anna", 45)
p2 = Person("Kirill", 23)
p3 = Person("Firuza", 16)
p4 = Person("Aigul", 48)
print(p.name, p.age)
print(p.name)
p.age = 1 #изменение свойств обьекта
del p1.age #удаление
print(p1.age)
print(p.age)
print(p.func1())
print(p1.func1())
print(p4.func1())