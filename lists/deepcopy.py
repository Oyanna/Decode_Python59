import copy

a = ['Анна', "Боря", "Оля"]
a2 = copy.deepcopy(a)
a2.append("Маша")
print(a)
print(a2)