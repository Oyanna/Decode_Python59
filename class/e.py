class Student:
    def __init__(self, surname, name, course, status):
        self.surname = surname
        self.name = name
        self.course = course
        self.status = status

    def statusOfSes(self):
        print ("Имя : {}. статус : {}".format(self.name, self.status))
a = Student("Иванов", "Петя", 3, "сдал")
b = Student("mdkd", "ehdjewhd", 1, "не сдал")

print(b.statusOfSes())
