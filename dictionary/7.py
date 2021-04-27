users = {
    "12": "Alice",
    "11": "Sasha",
    1:"Masha"
}
 #del users["10000"]
#print(users)
key = "12"
if key in users :
    user = users[key]
    del users[key]
    print(user, "успешно удален")
else:
    print("Такого пользователя нет")