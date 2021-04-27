key = "+5656565"
user_list =[
    ["+8783472834", "Anna"],
    ["476746", "Bob"],
    ["+877766", "Alice"]]
users = dict(user_list)
user = users.get("476746")

user = users.get("47674", "Ne znayu")
print(user)