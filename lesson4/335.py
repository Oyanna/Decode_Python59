import math
a = int(input())
b = int(input())
for i in range(a, b+1):
    c = math.sqrt(i)
    if c%1 == 0:
        print(i)