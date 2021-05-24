class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
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


class Teacher(Person):
    def __init__(self, name, age, school):
        Person.__init__(self, name, age)
        self.school = school
    def show_info(self):
        Person.show_info(self)
        print("Школа: ", self.school)

class Student(Person):
    def __init__(self, name, age,school, level):
        Person.__init__(self, name, age)
        self.school = school
        self.level = level
    def show_info(self):
        Person.show_info(self)
        print("Ученик", self.name, "учится в ", self.school, "школе в ", self.level, "классе")

people = [ Person("Ann", 77), Teacher("Zhuldyz", 49, 27), Student("Sasha", 7, 10, 1)]
for person in people:
    person.show_info()
    print()
for person in people:
    if isinstance(person, Student):
        print(person.school, person.level)
    elif isinstance(person, Teacher):
        print(person.school)
    else :
        print(person.name)
    print()