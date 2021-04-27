users = {
    "12": "Alice",
    "11": "Sasha",
    1:"Masha"
}
key = "11"
user = users.pop("12")
print(users)

user = users.pop("1123374631", "Unknown")
print(user)

users.clear()
print(users)

