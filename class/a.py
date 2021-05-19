class MyClass:
    x = 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        print("Привет, меня зовут " + self.name)

p = Person("Ayana", 20)
p1 = Person("Anna", 45)
p2 = Person("Kirill", 23)
p3 = Person("Firuza", 16)
p4 = Person("Aigul", 48)
print(p.name, p.age)
print(p.name)
print(p.age)
print(p.func1())
print(p1.func1())
print(p4.func1())
