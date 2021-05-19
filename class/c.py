class Employee:
    cnt = 0

    def __init__(self, surname, name, age, salary):
        self.surname = surname
        self.name = name
        self.age = age
        self.salary = salary
        Employee.cnt+=1
    def print_count(self):
        print("Всего сотрудников :  %d" % Employee.cnt)
    def print_empl(self):
        print("Имя : {}. Зарплата : {}".format(self.name, self.salary))


a = Employee("Kim", "Anna", 33, 150000)
b = Employee("Tsoy", "Nikita", 23, 250000)
b2 = Employee("Nam", "Olga", 29, 26000)
b3 = Employee("gfhgfg", "ghjgh", 29, 250000)
print(a.print_empl())
print(b.print_empl())
print(b.print_count())
