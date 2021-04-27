user_list =[
    ["+8783472834", "Anna"],
    ["476746", "Bob"],
    ["+877766", "Alice"]]
user_dict = dict(user_list)
print(user_dict)
print(user_dict["+8783472834"])
print(user_dict["476746"])
user_dict["+3943837"] = "Aigul"
print(user_dict)
#user = user_dict["+211111"]
key = "+211111"
if key in user_dict:
    user = user_dict["+211111"]
    print(user)
else:
    print("Не найден")

key1 = "476746"
if key1 in user_dict:
    user = user_dict["476746"]
    print(user)
else:
    print("Не найден")