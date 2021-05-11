dict1 = {1: 'val1', 2: 'val2', 3: "val3"}
dict1['key3'] = 12
print(dict1)

dict1[('gh', 'h', 'ghf')] = [11, 22, 'hi', 55.5, True]
print(dict1)

x = dict1[2]
print(x)
dict1[6] = [1, ]
z = dict1.pop(2, 'No')
print(dict1)


keys = dict1.keys()
print(keys)