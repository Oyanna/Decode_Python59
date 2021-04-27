users1 = {
    "12": "Alice",
    "11": "Sasha",
    1:"Masha"
}
users2 = {
    "8": "Alex",
    "7": "Dasha",
    2:"Pasha"
}
users3 = users1.copy()
users3.update(users2)
print(users1)
print(users2)
print(users3)