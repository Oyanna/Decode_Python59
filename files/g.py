filename = "example.txt"
spisok = list()

for i in range(3):
    a = input("Введите строку "+ str(i+1) + ":")
    spisok.append(a + "\n")

with open(filename, "a") as file:
    for a in spisok:
        file.write(a)

print("Считанные из файла данные")
with open(filename, "r") as file:
    for a in file:
        print(a, end="")