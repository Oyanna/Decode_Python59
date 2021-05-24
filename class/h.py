class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age in range(0, 120):
            self.__age = age
        else:
            print("Недопустимый возраст")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        x = name.isalpha()
        if x == False:
            print("Недопустимое имя")
        else:
            self.__name = name

    def show_info(self):
        print("Имя:", self.__name, "Возраст: ", self.__age)

a = Person("Anna")
a.show_info()
a.age = -200
a.name = "Tom"
a.show_info()

