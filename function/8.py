def sum(*params):
    result = 0
    for n in params:
        result+=n
    return result

a = sum(1, 2 , 3, 4, 5, 6)
print(a)
b = sum( 55, 44)
print(b)