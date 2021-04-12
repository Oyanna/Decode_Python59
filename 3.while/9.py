number = int(input("Ведите число : "))
i = 1
fact = 1
while i <= number :
    fact = fact * i
    i += 1
print("Факториал равен ", fact)