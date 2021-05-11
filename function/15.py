def func1():
    param = 4

    def inner():
        param += 1

    return param

def func2():
    param = 4

    def inner(a):
        a+=1
        print(a, "Значение внутр функ")

    inner(param)
    return param



def func3():
    param = 4
    def inner(a):
        a+=1
        return a
    param = inner(param)
    return param

print(func1())
print(func2())
print(func3())