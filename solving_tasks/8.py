list1 = [1, 1, 1, 1, 1, 1, 1]
list1.append("jhgdjed")
list1[5] = 123
print(list1)
list1.append(["a", "v"])
print(list1)
list1[3] = (1, 3)
print(list1)
list1.remove(1)
print(list1)

print(list1.count(1))