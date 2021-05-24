class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
    def set_age(self, age):
        if age in range(1, 120):
            self.__age = age
        else:
            print("НЕдопустимый возраст")

    def set_name(self, name):
        x = name.isalpha()
        if x == False:
            print("Недопустимое имя")
        else:
            self.__name = name
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def show_info(self):
        print("Имя:", self.__name, "Возраст: ", self.__age)

a = Person("Anna")
a.show_info()
a.set_age(14)
a.show_info()
print(a.get_name())
a.set_name("Alice")
print(a.show_info())
a.set_name('Flic3')

