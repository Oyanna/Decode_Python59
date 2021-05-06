a=[3, 10, "Sasha", "Vanya", 67]
print(a)

a=[3, 10, "Sasha", "Vanya", 67]
a.append("Lena")
print(a)

a=[3, 10, "Sasha", "Vanya", 67]
a.insert(1, 15)
print(a)

a=[3, 10, "Sasha", "Vanya", 67]
list=[1, 2, 3]
a.append(list)
print(a)

a=[3, 10, "Sasha", "Vanya", 67]
a.insert(2,["Vadim"])
print(a)

a=[5, 6, 3 ]
A=(3, 4, 8, -1, -4)
a.append(A)
print(a)

x=("Nigora", "Iroda", "Vika", "Erika")
print(x.index("Iroda"))

n=[1, 34, 58, 11]
print(n[0])

i = [i*3 for i in "privet" if i!="A"]
i.clear()
print(i)

list=[-3, 8, 9, 5]
list.remove(-3)
print(list)

n=[3, 3, 3, 90, 46, 39, 88]
print(n.count(3))
