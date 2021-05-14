with open("test", "r") as file:
    content = file.readlines()
    str1 = content[0]
    str2 = content[1]
    print(str1, end = "")
    print(str2)
    print(content)